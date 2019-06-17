---
layout: default
---
# Result Darknet network with good images and bad weather images


I trained the darknet network with good images and bad weather images . Then I used dl-detectionSuite for evaluating this network with good images and with bad weather conditions images. And I got the next results:

|           Images              |  mAP(Overall)(IOU=0.5) | mAR(Overall)(IOU=0.5) | Total images | Total samples| 
| ----------------------------- | ---------------------- | --------------------- | ------------ | ------------ |
|     Good images               |         0.775857       |          0.848839     |      389     |     1657     |
| Bad weather conditions        |         0.969699	 |          0.975368     |       71     |      287     |
| Bad weather conditions + Good |         0.795034	 |          0.858873     |      460     |     1944     |
