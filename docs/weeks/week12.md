---
layout: default
---
# Tensorflow - Smart traffic sensor



In the original smart-traffic-sensor, tensorflow is implemented in C++. When I trained my own database I used ([tensorflow/models](https://github.com/tensorflow/models)). tensorflow/models has been updated and it's incompatible wwith the tensorflow implementation in smart-traffic-sensor, because in this case an older version of tensorflow was used.
For this reason I have put tensorflow in python. Because if in the future tensorflow / models is updated again, we would be limited to the version that we place in smart-traffic-sensor. With Python we avoid this problem, since it is only necessary to update tensorflow in the computer.

In the next video you can see tensorflow in smart-traffic-sensor:

[![Smart-Traffic-Sensor Tensorflow1](https://roboticsurjc-students.github.io/2018-tfm-Jessica-Fernandez/images/tensorflow_smart_traffic_sensor.png)](https://www.youtube.com/watch?v=AyDBIZC3P2A&feature=youtu.be)
