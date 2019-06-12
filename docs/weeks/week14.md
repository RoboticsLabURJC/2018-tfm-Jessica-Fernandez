---
layout: default
---
# Tracking by detection


In smart-traffic-sensor I have implemented the tracking by detection using the detections of the deep learning and KLT(Kanade Lukas Tomasi) algorithm. For this I consider the following:
* All the image is for detection and tracking.
* In each image I detect with deep learning and I do the tracking using the distance. I compare all the blobs detected with the blobs saved in the before instant. The blob (detected in the image) that is more near of the tracked blob is the continuation of this tracked blob . For this I keep in mind that the blob detected is in the ellipse of the tracked blob. If I have lost a blob in the detection I use klt for recover it.
* If I have lost a blob with the detection during three sequences followed I consider that this blob is a wrong blob.
* If I have detected a new blob with deep learning this is a new vehicle. I mean, if there is a blob in the detections that I have not been able to match, I consider it a new vehicle.

Below you can see a video of its operation:

[![Tracking by detection](https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/docs/images/Tracking_by_detection.png)](https://www.youtube.com/watch?v=RVkaHOFigd4)
