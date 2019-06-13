---
layout: default
---
# Result Darknet network with good images 


I trained the darknet network with good images( good qualityand good weather conditions) . Then I used dl-detectionSuite for evaluating this network with good images and with bad weather conditions images. And I got the next results:

|           Images              |  mAP(Overall)(IOU=0.5) | mAR(Overall)(IOU=0.5) | Total images | Total samples| 
| ----------------------------- | ---------------------- | --------------------- | ------------ | ------------ |
|     Good images               |         0.819614       |          0.853816     |       71     |      287     |
| Bad weather conditions        |         0.913124	 |          0.933543     |      389     |     1657     |
| Bad weather conditions + Good |         0.821231	 |          0.856561     |      460     |     1944     |
