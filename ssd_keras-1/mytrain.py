from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from keras import backend as K
from keras.models import load_model
from math import ceil
import numpy as np
from keras_ssd7 import build_model
from keras_ssd_loss import SSDLoss
from ssd_box_encode_decode_utils import SSDBoxEncoder, decode_y, decode_y2
from ssd_batch_generator import BatchGenerator
import matplotlib.pyplot as plt
import argparse
import os
import cv2

CLASSES = ['background','stamp']
SCALES = [0.08,0.16,0.32,0.64,0.96] # An explicit list of anchor box scaling factors. If this is passed, it will override `min_scale` and `max_scale`.
ASPECT_RATIOS = [0.5,1.0,2.0] # The list of aspect ratios for the anchor boxes
VARIANCES = [1.0,1.0,1.0,1.0] # The list of variances by which the encoded target coordinates are scaled

curdir = os.path.dirname(os.path.abspath(__file__))
parser = argparse.ArgumentParser()
parser.add_argument('train_images')
parser.add_argument('test_images')
parser.add_argument('train_labels')
parser.add_argument('test_labels')
parser.add_argument(
    '--result',default=os.path.join(curdir,'result'))
parser.add_argument(
    '--epochs',type=int,default=10,
    help='Training epochs')
parser.add_argument(
    '--batch_size',type=int,default=32,
    help='Batch size')
parser.add_argument(
    '--img_height',type=int,default=225,
    help='Height of the input images')
parser.add_argument(
    '--img_width',type=int,default=525,
    help='Width of the input images')
parser.add_argument(
    '--img_channels',type=int,default=3,
    help='Number of color channels of the input images')
parser.add_argument(
    '--n_classes',type=int,default=2,
    help='Number of classes including the background class')
parser.add_argument(
    '--two_boxes_for_ar1',type=bool,default=True,
    help='Whether or not you want to generate two anchor boxes for aspect ratio 1')
parser.add_argument(
    '--limit_boxes',type=bool,default=False,
    help='Whether or not you want to limit the anchor boxes to lie entirely within the image boundaries')
parser.add_argument(
    '--coords',type=str,choices=['centroids','minmax'],default='centroids',
    help='Whether the box coordinates to be used should be in the \'centroids\' or \'minmax\' format, see documentation')
parser.add_argument(
    '--normalize_coords',type=bool,default=False,
    help='Whether or not the model is supposed to use relative coordinates that are within [0,1]')
parser.add_argument(
    '--pos_iou_threshold',type=float,default=0.5,
    help='IOU positive threshold')
parser.add_argument(
    '--neg_iou_threshold',type=float,default=0.2,
    help='IOU negative threshold')

def main(args):

    # ===============================
    # Instantiate model
    # ===============================
    # The output `predictor_sizes` is needed below to set up `SSDBoxEncoder`
    model, predictor_sizes = build_model(
        image_size=(args.img_height,args.img_width,args.img_channels),
        n_classes=args.n_classes,
        scales=SCALES,
        aspect_ratios_global=ASPECT_RATIOS,
        aspect_ratios_per_layer=None,
        two_boxes_for_ar1=args.two_boxes_for_ar1,
        limit_boxes=args.limit_boxes,
        variances=VARIANCES,
        coords=args.coords,
        normalize_coords=args.normalize_coords)

    model.compile(
        optimizer=Adam(decay=5e-5),
        loss=SSDLoss().compute_loss)

    # ===============================
    # Instantiate encoder
    # ===============================
    ssd_box_encoder = SSDBoxEncoder(
        img_height=args.img_height,
        img_width=args.img_width,
        n_classes=args.n_classes,
        predictor_sizes=predictor_sizes,
        scales=SCALES,
        aspect_ratios_global=ASPECT_RATIOS,
        aspect_ratios_per_layer=None,
        two_boxes_for_ar1=args.two_boxes_for_ar1,
        limit_boxes=args.limit_boxes,
        variances=VARIANCES,
        pos_iou_threshold=args.pos_iou_threshold,
        neg_iou_threshold=args.neg_iou_threshold,
        coords=args.coords,
        normalize_coords=args.normalize_coords)

    # ===============================
    # Prepare for Training
    # ===============================
    # training set
    train_dataset = BatchGenerator(
        box_output_format=['class_id', 'xmin', 'xmax', 'ymin', 'ymax'])
    train_dataset.parse_csv(
        images_path=args.train_images,
        labels_path=args.train_labels,
        input_format=['image_name','xmin','xmax','ymin','ymax','class_id'])
    train_generator = train_dataset.generate(
        batch_size=args.batch_size,
        train=True,
        ssd_box_encoder=ssd_box_encoder,
        equalize=True,
        brightness=(0.5, 2, 0.5), # Randomly change brightness between 0.5 and 2 with probability 0.5
        flip=0.5, # Randomly flip horizontally with probability 0.5
        translate=((5, 50), (3, 30), 0.5), # Randomly translate by 5-50 pixels horizontally and 3-30 pixels vertically with probability 0.5
        scale=(0.75, 1.3, 0.5), # Randomly scale between 0.75 and 1.3 with probability 0.5
        random_crop=False,
        crop=False,
        resize=(args.img_height,args.img_width),
        gray=False,
        limit_boxes=True,
        include_thresh=0.4,
        diagnostics=False)
    n_train_samples = train_dataset.get_n_samples()

    # validation set
    test_dataset = BatchGenerator(box_output_format=['class_id', 'xmin', 'xmax', 'ymin', 'ymax'])
    test_dataset.parse_csv(
        images_path=args.test_images,
        labels_path=args.test_labels,
        input_format=['image_name','xmin','xmax','ymin','ymax','class_id'])
    test_generator = test_dataset.generate(
        batch_size=args.batch_size,
        train=True,
        ssd_box_encoder=ssd_box_encoder,
        equalize=True,
        brightness=False,
        flip=False,
        translate=False,
        scale=False,
        random_crop=False,
        crop=False,
        resize=(args.img_height,args.img_width),
        gray=False,
        limit_boxes=True,
        include_thresh=0.4,
        diagnostics=False)
    n_test_samples = test_dataset.get_n_samples()

    # ===============================
    # Training
    # ===============================
    history = model.fit_generator(
        generator=train_generator,
        steps_per_epoch=ceil(n_train_samples/args.batch_size),
        epochs=args.epochs,
        callbacks=[ReduceLROnPlateau(monitor='val_loss',factor=0.5,patience=0,epsilon=1e-3,cooldown=0)],
        validation_data=test_generator,
        validation_steps=ceil(n_test_samples/args.batch_size))

    # ===============================
    # Save results
    # ===============================
    if os.path.exists(args.result) == False:
        os.makedirs(args.result)
    model.save(os.path.join(args.result,'model.h5'))
    model.save_weights(os.path.join(args.result,'weights.h5'))

    # ===============================
    # Test detection
    # ===============================
    test_dir = os.path.join(args.result,'test')
    if os.path.exists(test_dir) == False:
        os.makedirs(test_dir)
    predict_generator = test_dataset.generate(
        batch_size=1,
        train=False,
        equalize=True,
        brightness=False,
        flip=False,
        translate=False,
        scale=False,
        random_crop=False,
        crop=False,
        resize=(args.img_height,args.img_width),
        gray=False,
        limit_boxes=True,
        include_thresh=0.4,
        diagnostics=False)

    for i in range(n_test_samples):
        print('test detection (%d/%d):' % (i+1,n_test_samples))
        x, y_true, filenames = next(predict_generator)
        y_pred = model.predict(x)
        y_pred_decoded = decode_y2(
            y_pred,
            confidence_thresh=0.5,
            iou_threshold=0.4,
            top_k=1,
            input_coords='centroids',
            normalize_coords=False,
            img_height=None,
            img_width=None)
        plt.figure(figsize=(20,12))
        plt.imshow(x[0])
        current_axis = plt.gca()

        # Draw the predicted boxes in blue
        for box in y_pred_decoded[0]:
            class_id = int(box[0])
            confidence = box[1]
            xmin,xmax = int(box[2]),int(box[3])
            ymin,ymax = int(box[4]),int(box[5])
            label = '%s:%2f' % (CLASSES[class_id],confidence)
            current_axis.add_patch(plt.Rectangle(
                (xmin, ymin),xmax-xmin,ymax-ymin,color='blue',fill=False,linewidth=2))
            current_axis.text(
                xmin,ymin,label,size='x-large',color='white',bbox={'facecolor':'blue','alpha':1.0})
        plt.savefig(os.path.join(test_dir,os.path.basename(filenames[0])))
        print('saved in %s' % (os.path.join(test_dir,os.path.basename(filenames[0]))))
        plt.clf()


if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
