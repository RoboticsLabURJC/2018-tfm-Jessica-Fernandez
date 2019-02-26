from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau, TerminateOnNaN, CSVLogger
from keras import backend as K
from keras.models import load_model
from math import ceil
import numpy as np
from matplotlib import pyplot as plt

from models.keras_ssd7 import build_model
from keras_loss_function.keras_ssd_loss import SSDLoss
from keras_layers.keras_layer_AnchorBoxes import AnchorBoxes
from keras_layers.keras_layer_DecodeDetections import DecodeDetections
from keras_layers.keras_layer_DecodeDetectionsFast import DecodeDetectionsFast

from ssd_encoder_decoder.ssd_input_encoder import SSDInputEncoder
from ssd_encoder_decoder.ssd_output_decoder import decode_detections, decode_detections_fast

from data_generator.object_detection_2d_data_generator import DataGenerator
from data_generator.object_detection_2d_misc_utils import apply_inverse_transforms
from data_generator.data_augmentation_chain_variable_input_size import DataAugmentationVariableInputSize
from data_generator.data_augmentation_chain_constant_input_size import DataAugmentationConstantInputSize
from data_generator.data_augmentation_chain_original_ssd import SSDDataAugmentation

if __name__ == '__main__':
	img_height = 520 # Height of the input images
	img_width = 520 # Width of the input images
	img_channels = 3 # Number of color channels of the input images
	n_classes = 7 # Number of classes including the background class
	min_scale = 0.08 # The scaling factor for the smallest anchor boxes
	max_scale = 0.96 # The scaling factor for the largest anchor boxes
	scales = [0.08, 0.16, 0.32, 0.64, 0.96] # An explicit list of anchor box scaling factors. If this is passed, it will override `min_scale` and `max_scale`.
	aspect_ratios = [0.5, 1.0, 2.0] # The list of aspect ratios for the anchor boxes
	two_boxes_for_ar1 = True # Whether or not you want to generate two anchor boxes for aspect ratio 1
	limit_boxes = False # Whether or not you want to limit the anchor boxes to lie entirely within the image boundaries
	variances = [1.0, 1.0, 1.0, 1.0] # The list of variances by which the encoded target coordinates are scaled
	coords = 'centroids' # Whether the box coordinates to be used should be in the 'centroids' or 'minmax' format, see documentation
	normalize_coords = False # Whether or not the model is supposed to use relative coordinates that are within [0,1]

	K.clear_session() # Clear previous models from memory.
	# TODO: Set the path to the `.h5` file of the model to be loaded.
	model_path = 'ssd7_1000.h5'

	# We need to create an SSDLoss object in order to pass that to the model loader.
	ssd_loss = SSDLoss(neg_pos_ratio=3, alpha=1.0)

	K.clear_session() # Clear previous models from memory.
	
	# The directories that contain the images.
	images_dir      = '/home/docker/Jessi/smart-traffic-sensor-lab/vehicles-dataset/images/'

	# The directories that contain the annotations.
	annotations_dir      = '/home/docker/Jessi/smart-traffic-sensor-lab/vehicles-dataset/annotations/'

	# The paths to the image sets.
	train_image_set_filename    = '/home/docker/Jessi/ssd_keras-1/train.txt'
	test_image_set_filename      = '/home/docker/Jessi/ssd_keras-1/test.txt'

	classes = ['None','motorcycle', 'car','van', 'bus', 'truck',
		   'small-truck', 'tank-truck']

	model = load_model(model_path, custom_objects={'AnchorBoxes': AnchorBoxes,
		                                       'compute_loss': ssd_loss.compute_loss})
	#model.load_weights('ssd7_100_weights.h5')
	val_dataset = DataGenerator(load_images_into_memory=False, hdf5_dataset_path=None)
	val_dataset.parse_xml(images_dirs=[images_dir],
			      image_set_filenames = [test_image_set_filename],
		              annotations_dirs=[annotations_dir],
		              classes=classes,
		              include_classes='all',
		              exclude_truncated=False,
		              exclude_difficult=False,
		              ret=False)
	predict_generator = val_dataset.generate(batch_size=1,
                                         shuffle=True,
                                         transformations=[],
                                         label_encoder=None,
                                         returns={'processed_images',
                                                  'processed_labels',
                                                  'filenames'},
                                         keep_images_without_gt=False)


	batch_images, batch_labels, batch_filenames = next(predict_generator)

	i = 0 # Which batch item to look at

	print("Image:", batch_filenames[i])
	print()
	print("Ground truth boxes:\n")
	print(batch_labels[i])
	# 3: Make a prediction
	print((batch_images[i].shape),batch_images.shape)
	y_pred = model.predict(batch_images)
	print (y_pred)
	# 4: Decode the raw prediction `y_pred`

	y_pred_decoded = decode_detections(y_pred,
		                           confidence_thresh=0.3,
		                           iou_threshold=None,
		                           top_k=200,
		                           normalize_coords=normalize_coords,
		                           img_height=img_height,
		                           img_width=img_width)

	# 5: Draw the predicted boxes onto the image

	plt.figure(figsize=(20,12))
	plt.imshow(batch_images[i])
	

	current_axis = plt.gca()

	colors = plt.cm.hsv(np.linspace(0, 1, n_classes+1)).tolist() # Set the colors for the bounding boxes

	

	# Draw the predicted boxes in blue
	for box in y_pred_decoded[i]:
	    print('box',box)
	    xmin = box[-4]
	    ymin = box[-3]
	    xmax = box[-2]
	    ymax = box[-1]
            print('data',xmin,ymin,xmax,ymax, box[0], box[1])
	    color = colors[int(box[0])]
	    label = '{}: {:.2f}'.format(classes[int(box[0])], box[1])
	    current_axis.add_patch(plt.Rectangle((xmin, ymin), xmax-xmin, ymax-ymin, color=color, fill=False, linewidth=1))  
	    current_axis.text(xmin, ymin, label, size='x-large', color='white', bbox={'facecolor':color, 'alpha':1.0})

	plt.show()
