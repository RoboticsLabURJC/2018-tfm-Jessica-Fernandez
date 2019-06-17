---
layout: default
---
# Result Darknet network with good images 


I trained the darknet network with good images( good quality and good weather conditions) . Then I used dl-detectionSuite for evaluating this network with good images and with bad weather conditions images. And I got the next results:

|           Images              |  mAP(Overall)(IOU=0.5) | mAR(Overall)(IOU=0.5) | Total images | Total samples| 
| ----------------------------- | ---------------------- | --------------------- | ------------ | ------------ |
|     Good images               |         0.920018       |          0.949379     |      389     |     1657     |
| Bad weather conditions        |         0.89859	 |          0.937896     |       71     |      287     |
| Bad weather conditions + Good |         0.917103	 |          0.948178     |      460     |     1944     |
