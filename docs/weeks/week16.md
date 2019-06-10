---
layout: default
---
# Smart-traffic-sensor Evaluation 


I used ([dl-DetectionSuite](https://github.com/JdeRobot/dl-DetectionSuite)) to evaluate smart-traffic-sensor. I have compared the deep learning smart-traffic-sensor and the klt smart-traffic-sensor. I only considered the results for an IOU of 0.5 . And I got the next results:

|        Network        |  mAP(Overall)(IOU=0.5) | mAR(Overall)(IOU=0.5) | 
| --------------------- | ---------------------- | -------------------------- | 
|     Deep Learning     |         0.90878	 |          0.914015          |    
|          KLT          |         0.404088	 |          0.544972          | 
