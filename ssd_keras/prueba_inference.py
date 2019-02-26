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
		        mode='inference',
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
	weights_path = 'ssd300adam_1000_cambio_ancho_coco_120_weights.h5'

	model.load_weights(weights_path, by_name=True)
	adam = Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=5e-04)
	#sgd = SGD(lr=0.001, momentum=0.9, decay=0.0, nesterov=False)

	ssd_loss = SSDLoss(neg_pos_ratio=3, alpha=1.0,n_neg_min=0)

	model.compile(optimizer=adam, loss=ssd_loss.compute_loss,metrics=['mae','accuracy'])
	# Optional: If you have enough memory, consider loading the images into memory for the reasons explained above.
	

	classes = ['None','motorcycle','car', 'van', 'bus', 'truck',
		   'small-truck', 'tank-truck']

	
	model_name = 'ssd300adam_1000_cambio_ancho_coco_120_inference'
	model.save('./{}.h5'.format(model_name))
	model.save_weights('./{}_weights.h5'.format(model_name))
	

