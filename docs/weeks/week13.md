---
layout: default
---
# Autoevaluator- dl-DetectionSuite. Test 1


I used ([dl-DetectionSuite](https://github.com/JdeRobot/dl-DetectionSuite)) to compare the different model that I have. In this ocasion I haven't had the far cars in account. Also I have evaluated the pretrained networks that I used to do the training. With this condition I got the next results:

|        Network        |  mAP(Overall)(IOU=0.5:0.95) | mAR(Overall)(IOU=0.5:0.95) | Mean inference time (ms) | 
| --------------------- | --------------------------- | -------------------------- | ------------------------ |
|          Keras        |           0.617666	      |          0.653703          |           3427           | 
|          Yolo         |           0.56836	      |          0.615658          |           16894          |
|       Tensorflow      |           0.454884	      |          0.490377          |            76            |  
|    Keras-Pretrained   |              0	      |              0             |             0            | 
|    Yolo-Pretrained    |              0	      |              0             |           14162          |
| Tensorflow-Pretrained |           0.0141532	      |          0.0398529         |            142           |  
