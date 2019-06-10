---
layout: default
---
# Tracking by detection 1


It has been added that the boxes appear in the vehicles. Also I changed some things:
* If I have lost a blob with the detection during five sequences followed I consider that this blob is a wrong blob.

Below you can see the result:

[![Tracking by detection1](https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/docs/Tracking_by_detection1.png)](https://www.youtube.com/watch?v=ReM2HAbOo-s)

I have measured the detection + tracking times for the different methods, obtaining the following:

|         Method        |  Tracking + Detection Time (ms) | 
| --------------------- | ------------------------------- |
|          Keras        |                45               |        
|          Yolo         |                48	          |        
|       Tensorflow      |                20	          |    
|           KLT         |                5	          | 
