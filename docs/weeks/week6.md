---
layout: default
---
# Smart-traffic-sensor Darknet


[Darknet](https://pjreddie.com/darknet/) is an open source neural network framework written in C. Darknet supports both GPU and CPU builds. You can install it following the instructions below:

```ruby
  git clone https://github.com/JdeRobot/darknet
  cd darknet
  mkdir build && cd build
For GPU users:
  cmake -DCMAKE_INSTALL_PREFIX=/usr/local -DUSE_GPU=ON ..
For CPU users:
  cmake -DCMAKE_INSTALL_PREFIX=/usr/local -DUSE_GPU=OFF ..
  
  make -j4
  sudo make -j4 install
```

For Darknet you need a weights file, a config file and a label file. In my case I tried yolov2-tiny.weights, yolov2-tiny.cfg ([Tiny YOLO](https://pjreddie.com/darknet/yolo/)) and  [COCO ClassNames File](https://raw.githubusercontent.com/wiki/JdeRobot/dl-DetectionSuite/coco.names). I did a test with this neuronal network in smart-traffic-sensor:

[![Smart-Traffic-Sensor Darknet integration](https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/docs/images/Darknet_integration.png)](https://www.youtube.com/watch?v=j7X3t8OMXaE&feature=youtu.be)
