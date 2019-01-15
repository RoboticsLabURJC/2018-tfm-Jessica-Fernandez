# 2018-tfm-Jessica-Fernandez
## Week 1
To start I downloaded the component Object Detector (https://github.com/JdeRobot/dl-objectdetector). In this component, you can upload the model of your neural network and the captured image of a webcam or video to test how your neural network works. In mi case I used a ssdlite_mobilenet_v2_coco_2018_05_29.pb model and a traffic video. In the next image you can see an example:

![Object_detector](https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/docs/Captura%20de%20pantalla%20de%202018-10-12%2018-26-54.png)

## Week 2
I'm labelling some traffic images for creating a database. For this, I use labelImg(https://github.com/tzutalin/labelImg).

![labelImg](https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/docs/Captura%20de%20pantalla%20de%202018-11-03%2014-29-36.png)

## Week 3
I have been integrating keras in smart-traffic-sensor. For this, I have to embeded Python code in C++. You can find information in the following links: https://docs.python.org/2/extending/embedding.html , https://realmike.org/blog/2012/07/05/supercharging-c-code-with-embedded-python/ , https://www.codeproject.com/Articles/11805/Embedding-Python-in-C-C-Part-I. You can see a basic example in the next code (hello_python.cpp):
```ruby
#include <stdio.h>
#include <python3.5/Python.h>

int main()
{
	PyObject* pInt;
	Py_Initialize();
	PyRun_SimpleString("print('Hello World from Embedded Python!!!')");
	Py_Finalize();
	printf("\nPress any key to exit...\n");
}
```
You have to compile in the following way: 
```ruby
gcc hello_python.cpp -o hello_python -L/usr/lib/python2.7/config/ -lpython2.7
```
The result is:
```ruby
Hello World from Embedded Python!!!
Press any key to exit...
```
At the moment, I have used a COCO model(VGG_300_300_coco.h5 -> http://jderobot.org/store/deeplearning-networks/Keras/) for keras in a traffic video. At the moment I have used a coconut model for keras in a traffic video. Although I still have some conflict with the part of tensorflow already integrated, because in the part of keras some tensorflow function is also used and I am getting some problems by leaving both parts enabled. In the next video, you can see an example:

[![Smart-Traffic-Sensor With Keras. First Example](https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/docs/Captura%20de%20pantalla%20de%202018-11-19%2022-35-38.png)](https://www.youtube.com/watch?v=0MeZSVHg-3M)

## Neuronal Network with Keras

I have been looking for neuronal networks with keras for objects detection. Currently the ssd networks are having great success, so I've tried these networks. For this I have based on: https://github.com/pierluigiferrari/ssd_keras . I did some tests.

### 1º Test
I tried the ssd300 with 1000 steps per epochs, 70 epochs and adam. I used the parameters, which are in the ssd300 example and I get the next result:

[![Smart-Traffic-Sensor With SSD300 Keras. First Example](https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/docs/keras1.png)](https://www.youtube.com/watch?v=qZrhYQ3WXGc&feature=youtu.be)


### 2º Test
I tried the ssd300 with 1000 steps per epochs, 120 epochs and SGD. I used the parameters, which are in the ssd300 example and I get the next result:

[![Smart-Traffic-Sensor With SSD300 Keras. Second Example](https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/docs/keras2.png)](https://www.youtube.com/watch?v=nEIczwMrbWc&feature=youtu.be)

### 3º Test
I tried the ssd7 with 1000 steps per epochs, 20 epochs and Adam. I used the parameters, which are in the ssd7 example and I get the next result:

[![Smart-Traffic-Sensor With SSD7 Keras. Example](https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/docs/keras3.png)](https://www.youtube.com/watch?v=71yQjBs76Vo&feature=youtu.be)

### 4º Test
I tried the ssd300 with 1000 steps per epochs, 70 epochs and Adam. In this case the steps parameter is None, the offsets parameter is None and I used the coco scales.

[![Smart-Traffic-Sensor With SSD300 Keras.Third Example](https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/docs/keras4.png)](https://www.youtube.com/watch?v=zGyK0PKNP7I&feature=youtu.be)

### 5º Test
I tried the ssd300 with 1000 steps per epochs, 120 epochs and Adam. In this case the steps parameter is None, the offsets parameter is None and I used the coco scales.

[![Smart-Traffic-Sensor With SSD300 Keras.Four Example](https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/docs/keras5.png)](https://www.youtube.com/watch?v=-tzJgebQSmw&feature=youtu.be)

## Smart-traffic-sensor Keras
I tested my keras model ( the 5º test) on the smart-traffic-sensor.Below you can see a video:

[![Smart-Traffic-Sensor Keras](https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/docs/smart_traffic_sensor_keras.png)](https://www.youtube.com/watch?v=pa6c3zmug8w&feature=youtu.be)

## Smart-traffic-sensor Darknet
Darknet (https://pjreddie.com/darknet/) is an open source neural network framework written in C. Darknet supports both GPU and CPU builds. You can install it following the instructions below:

```ruby
  git clone https://github.com/JdeRobot/darknet
  cd darknet
  mkdir build && cd build

```
