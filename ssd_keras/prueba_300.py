from keras.optimizers import Adam, SGD
from keras.callbacks import ModelCheckpoint, LearningRateScheduler, TerminateOnNaN, CSVLogger, ReduceLROnPlateau
from keras import backend as K
from keras.models import load_model
from math import ceil
import numpy as np
from matplotlib import pyplot as plt

from models.keras_ssd300 import ssd_300
from keras_loss_function.keras_ssd_loss import SSDLoss
from keras_layers.keras_layer_AnchorBoxes import AnchorBoxes
from keras_layers.keras_layer_DecodeDetections import DecodeDetections
from keras_layers.keras_layer_DecodeDetectionsFast import DecodeDetectionsFast
from keras_layers.keras_layer_L2Normalization import L2Normalization

from ssd_encoder_decoder.ssd_input_encoder import SSDInputEncoder
from ssd_encoder_decoder.ssd_output_decoder import decode_detections, decode_detections_fast

from data_generator.object_detection_2d_data_generator import DataGenerator
from data_generator.object_detection_2d_geometric_ops import Resize
from data_generator.object_detection_2d_photometric_ops import ConvertTo3Channels
from data_generator.data_augmentation_chain_original_ssd import SSDDataAugmentation
from data_generator.object_detection_2d_misc_utils import apply_inverse_transforms

def lr_schedule(epoch):
    if epoch < 300:
        return 0.001
    elif epoch < 500:
        return 0.0001
    else:
        return 0.00001

if __name__ == '__main__':

	img_height = 520 # Height of the model input images
	img_width = 520 # Width of the model input images
	img_channels = 3 # Number of color channels of the model input images
	mean_color = [123, 117, 104] # The per-channel mean of the images in the dataset. Do not change this value if you're using any of the pre-trained weights.
	
	n_classes = 8 # Number of positive classes, e.g. 20 for Pascal VOC, 80 for MS COCO
	scales_pascal = [0.1, 0.2, 0.37, 0.54, 0.71, 0.88, 1.05] # The anchor box scaling factors used in the original SSD300 for the Pascal VOC datasets
	scales_coco = [0.07, 0.15, 0.33, 0.51, 0.69, 0.87, 1.05] # The anchor box scaling factors used in the original SSD300 for the MS COCO datasets
	scales = scales_coco
	aspect_ratios = [[1.0, 2.0, 0.5],
                 [1.0, 2.0, 0.5, 3.0, 1.0/3.0],
                 [1.0, 2.0, 0.5, 3.0, 1.0/3.0],
                 [1.0, 2.0, 0.5, 3.0, 1.0/3.0],
                 [1.0, 2.0, 0.5],
                 [1.0, 2.0, 0.5]] # The anchor box aspect ratios used in the original SSD300; the order matters
	two_boxes_for_ar1 = True
	#steps = [8, 16, 32, 64, 100, 300] # The space between two adjacent anchor box center points for each predictor layer.
	#offsets = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5] # The offsets of the first anchor box center points from the top and left borders of the image as a fraction of the step size for each predictor layer.
	steps = None 
	offsets = None

	clip_boxes = False # Whether or not to clip the anchor boxes to lie entirely within the image boundaries
	variances = [0.1, 0.1, 0.2, 0.2] # The variances by which the encoded target coordinates are divided as in the original implementation
	normalize_coords = True
	

	# 1: Build the Keras model.

	K.clear_session() # Clear previous models from memory.

	model,predictor_sizes = ssd_300(image_size=(img_height, img_width, img_channels),
		        n_classes=n_classes,
		        mode='training',
		        l2_regularization=0.0005,
		        scales=scales,
		        aspect_ratios_per_layer=aspect_ratios,
		        two_boxes_for_ar1=two_boxes_for_ar1,
		        steps=steps,
		        offsets=offsets,
		        clip_boxes=clip_boxes,
		        variances=variances,
		        normalize_coords=normalize_coords,
		        subtract_mean=mean_color,
			confidence_thresh=0.5,
			iou_threshold=0.45)

	# 3: Instantiate an optimizer and the SSD loss function and compile the model.
	#    If you want to follow the original Caffe implementation, use the preset SGD
	#    optimizer, otherwise I'd recommend the commented-out Adam optimizer.
	print (model.summary())
	weights_path = 'VGG_ILSVRC_16_layers_fc_reduced.h5'

	model.load_weights(weights_path, by_name=True)
	adam = Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=5e-04)
	#sgd = SGD(lr=0.001, momentum=0.9, decay=0.0, nesterov=False)

	ssd_loss = SSDLoss(neg_pos_ratio=3, alpha=1.0,n_neg_min=0)

	model.compile(optimizer=adam, loss=ssd_loss.compute_loss,metrics=['mae','accuracy'])
	# Optional: If you have enough memory, consider loading the images into memory for the reasons explained above.
	print('output shape', model.output_shape)
	train_dataset = DataGenerator(load_images_into_memory=False, hdf5_dataset_path=None)
	val_dataset = DataGenerator(load_images_into_memory=False, hdf5_dataset_path=None)
	# The directories that contain the images.
	images_dir      = '/home/docker/Jessi/smart-traffic-sensor-lab/vehicles-dataset/images/'

	# The directories that contain the annotations.
	annotations_dir      = '/home/docker/Jessi/smart-traffic-sensor-lab/vehicles-dataset/annotations/'

	# The paths to the image sets.
	train_image_set_filename    = '/home/docker/Jessi/smart-traffic-sensor-lab/train.txt'
	test_image_set_filename      = '/home/docker/Jessi/smart-traffic-sensor-lab/test.txt'

	classes = ['None','motorcycle','car', 'van', 'bus', 'truck',
		   'small-truck', 'tank-truck']

	batch_size = 8

	train_dataset.parse_xml(images_dirs=[images_dir],
				image_set_filenames = [train_image_set_filename],
		                annotations_dirs=[annotations_dir],
		                classes=classes,
		                include_classes='all',
		                exclude_truncated=False,
		                exclude_difficult=False,
		                ret=False)
	# 6: Create the validation set batch generator (if you want to use a validation dataset)

	
	val_dataset.parse_xml(images_dirs=[images_dir],
			      image_set_filenames = [test_image_set_filename],
		              annotations_dirs=[annotations_dir],
		              classes=classes,
		              include_classes='all',
		              exclude_truncated=False,
		              exclude_difficult=False,
		              ret=False)

	# Optional: Convert the dataset into an HDF5 dataset. This will require more disk space, but will
	# speed up the training. Doing this is not relevant in case you activated the `load_images_into_memory`
	# option in the constructor, because in that cas the images are in memory already anyway. If you don't
	# want to create HDF5 datasets, comment out the subsequent two function calls.

	train_dataset.create_hdf5_dataset(file_path='dataset_pascal_voc_07+12_trainval.h5',
		                          resize=False,
		                          variable_image_size=True,
		                          verbose=True)

	val_dataset.create_hdf5_dataset(file_path='dataset_pascal_voc_07_test.h5',
		                        resize=False,
		                        variable_image_size=True,
		                        verbose=True)

	# 4: Set the image transformations for pre-processing and data augmentation options.

	# For the training generator:
	ssd_data_augmentation = SSDDataAugmentation(img_height=img_height,
		                                    img_width=img_width,
		                                    background=mean_color)
	# For the validation generator:
	convert_to_3_channels = ConvertTo3Channels()
	resize = Resize(height=img_height, width=img_width)

	# 5: Instantiate an encoder that can encode ground truth labels into the format needed by the SSD loss function.

	# The encoder constructor needs the spatial dimensions of the model's predictor layers to create the anchor boxes.
	predictor_sizes = [model.get_layer('conv4_3_norm_mbox_conf').output_shape[1:3],
		           model.get_layer('fc7_mbox_conf').output_shape[1:3],
		           model.get_layer('conv6_2_mbox_conf').output_shape[1:3],
		           model.get_layer('conv7_2_mbox_conf').output_shape[1:3],
		           model.get_layer('conv8_2_mbox_conf').output_shape[1:3],
		           model.get_layer('conv9_2_mbox_conf').output_shape[1:3]]


	ssd_input_encoder = SSDInputEncoder(img_height=img_height,
                                    img_width=img_width,
                                    n_classes=n_classes,
                                    predictor_sizes=predictor_sizes,
                                    scales=scales,
                                    aspect_ratios_per_layer=aspect_ratios,
                                    two_boxes_for_ar1=two_boxes_for_ar1,
                                    steps=steps,
                                    offsets=offsets,
                                    clip_boxes=clip_boxes,
                                    variances=variances,
                                    matching_type='multi',
                                    pos_iou_threshold=0.5,
                                    neg_iou_limit=0.5,
                                    normalize_coords=normalize_coords)

	# 6: Create the generator handles that will be passed to Keras' `fit_generator()` function.

	train_generator = train_dataset.generate(batch_size=batch_size,
		                                 shuffle=True,
						 transformations=[ssd_data_augmentation],
		                                 label_encoder=ssd_input_encoder,
		                                 returns={'processed_images',
		                                          'encoded_labels'},
		                                 keep_images_without_gt=False)

	val_generator = val_dataset.generate(batch_size=batch_size,
		                             shuffle=False,
					     transformations=[convert_to_3_channels,
                                                      resize],
		                             label_encoder=ssd_input_encoder,
		                             returns={'processed_images',
		                                      'encoded_labels'},
		                             keep_images_without_gt=False)

	# Get the number of samples in the training and validations datasets.
	train_dataset_size = train_dataset.get_dataset_size()
	val_dataset_size   = val_dataset.get_dataset_size()

	print("Number of images in the training dataset:\t{:>6}".format(train_dataset_size))
	print("Number of images in the validation dataset:\t{:>6}".format(val_dataset_size))

	# Define model callbacks.

	# TODO: Set the filepath under which you want to save the model.
	model_checkpoint = ModelCheckpoint(filepath='ssd300_pascal_07+12_epoch-{epoch:02d}_loss-{loss:.4f}_val_loss-{val_loss:.4f}.h5',
		                           monitor='val_loss',
		                           verbose=1,
		                           save_best_only=True,
		                           save_weights_only=False,
		                           mode='auto',
		                           period=1)
	#model_checkpoint.best = 

	csv_logger = CSVLogger(filename='ssd300_pascal_07+12_training_log.csv',
		               separator=',',
		               append=True)

	learning_rate_scheduler = LearningRateScheduler(schedule=lr_schedule,
		                                        verbose=1)

	terminate_on_nan = TerminateOnNaN()

	callbacks = [model_checkpoint,
		     csv_logger,
		     learning_rate_scheduler,
		     terminate_on_nan]
	# If you're resuming a previous training, set `initial_epoch` and `final_epoch` accordingly.
	initial_epoch   = 0
	final_epoch     = 70
	steps_per_epoch = 1000

	history = model.fit_generator(generator=train_generator,
			      steps_per_epoch=steps_per_epoch,
                              epochs=final_epoch,
                              callbacks=callbacks,
                              validation_data=val_generator,
                              validation_steps=ceil(val_dataset_size/batch_size),
                              initial_epoch=initial_epoch)

	model_name = 'ssd300adam_1000_cambio_ancho_coco_70'
	model.save('./{}.h5'.format(model_name))
	model.save_weights('./{}_weights.h5'.format(model_name))
	score = model.evaluate_generator(generator = val_generator,steps =ceil(val_dataset_size/batch_size), verbose=0)
	print('Test score:', score[0])
	print('Test mean absolute error:', score[1])
	print('Test accuracy:', score[2])
	print("score total",score)



