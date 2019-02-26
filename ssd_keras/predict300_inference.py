import cv2
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau, TerminateOnNaN, CSVLogger
from keras import backend as K
from keras.models import load_model
from math import ceil
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from keras.preprocessing import image

from models.keras_ssd7 import build_model
from models.keras_ssd300 import ssd_300
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
from keras_layers.keras_layer_L2Normalization import L2Normalization

path = '/home/docker/Jessi/smart-traffic-sensor/traffic-videos/video-0042-o-4.MPG'
cap = cv2.VideoCapture(path)
# Almacenamos las dimensiones de los frames del video.
alto=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT ))
ancho=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH ))

# Indicamos las caracteristicas de como se guardara el video
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I','D')
out = cv2.VideoWriter('video.avi',fourcc, 15.0, (ancho,alto))
model_path = 'ssd300adam_1000_cambio_ancho_coco_120_inference.h5'
img_height = 520 # Height of the input images
img_width = 520 # Width of the input images
img_channels = 3 # Number of color channels of the input images
n_classes = 8 # Number of classes including the background class
factor_height = np.true_divide(alto,img_height)
factor_width = np.true_divide(ancho,img_width)


min_scale = 0.08 # The scaling factor for the smallest anchor boxes
max_scale = 0.96 # The scaling factor for the largest anchor boxes
scales = [0.08, 0.16, 0.32, 0.64, 0.96] # An explicit list of anchor box scaling factors. If this is passed, it will override `min_scale` and `max_scale`.
aspect_ratios = [0.5, 1.0, 2.0] # The list of aspect ratios for the anchor boxes
two_boxes_for_ar1 = True # Whether or not you want to generate two anchor boxes for aspect ratio 1
limit_boxes = False # Whether or not you want to limit the anchor boxes to lie entirely within the image boundaries
variances = [1.0, 1.0, 1.0, 1.0] # The list of variances by which the encoded target coordinates are scaled
coords = 'centroids' # Whether the box coordinates to be used should be in the 'centroids' or 'minmax' format, see documentation
normalize_coords = True # W
classes = ['None','motorcycle', 'car','van', 'bus', 'truck',
		   'small-truck', 'tank-truck']
# We need to create an SSDLoss object in order to pass that to the model loader.
ssd_loss = SSDLoss(neg_pos_ratio=3, alpha=1.0)
K.clear_session() # Clear previous models from memory.

#model = load_model(model_path, custom_objects={'AnchorBoxes': AnchorBoxes,
#		                                       'compute_loss': ssd_loss.compute_loss})
model = load_model(model_path, custom_objects={'AnchorBoxes': AnchorBoxes,
						'L2Normalization': L2Normalization,
						 'DecodeDetections': DecodeDetections,
						  'compute_loss': ssd_loss.compute_loss})
# Recorremos todos los frames del video.
while(cap.isOpened()):
    ret,frame =cap.read()
    # Si el frame es correcto detectaremos el objeto de interes
    if ret == True:
	frame2 = cv2.resize(frame, (520, 520))
	frame1 = np.expand_dims(frame2, axis=0)

	#print(type(frame1),frame1.shape)
        y_pred = model.predict(frame1)
	#print('y pred',y_pred[0].shape,y_pred)
	#print(y_pred[0,:,1] )
	# 4: Decode the raw prediction `y_pred`
	confidence_threshold = 0.5
        # which predictions are above the confidence threshold?
        y_pred_decoded = [y_pred[k][y_pred[k,:,1] > confidence_threshold] for k in range(y_pred.shape[0])]
	
	
        # Mostramos el video y lo guardamos.
        print(y_pred_decoded[0])

	# Draw the predicted boxes in blue
	for box in y_pred_decoded[0]:
	    #print('box',box)
        
	    xmin = int(box[2] * factor_width)
            ymin = int(box[3] * factor_height)
            xmax = int(box[4] * factor_width)
            ymax = int(box[5] * factor_height)
            label = '{}: {:.2f}'.format(classes[int(box[0])], box[1])
	    cv2.putText(frame, str(label), (int(xmin+5), int(ymin-5)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 0, 255), 1)
	   # color = colors[int(box[0])]
	   # label = '{}: {:.2f}'.format(classes[int(box[0])], box[1])
	   # current_axis.add_patch(plt.Rectangle((xmin, ymin), xmax-xmin, ymax-ymin, color=color, fill=False, linewidth=1))  
	   # current_axis.text(xmin, ymin, label, size='x-large', color='white', bbox={'facecolor':color, 'alpha':1.0})

	
    	cv2.imshow("images", frame)
	#out.write(frame)
	#cv2.waitKey(0)
    else:
        break
    # Si se pulsa la q se sale del video.
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
#out.release()
cv2.destroyAllWindows()
