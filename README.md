# 2018-tfm-Jessica-Fernandez
## Week 1
To start I downloaded the component [Object Detector](https://github.com/JdeRobot/dl-objectdetector). In this component, you can upload the model of your neural network and the captured image of a webcam or video to test how your neural network works. In mi case I used a ssdlite_mobilenet_v2_coco_2018_05_29.pb model and a traffic video. In the next image you can see an example:

![Object_detector](https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/docs/Captura%20de%20pantalla%20de%202018-10-12%2018-26-54.png)

## Week 2
I'm labelling some traffic images for creating a database. For this, I use [labelImg](https://github.com/tzutalin/labelImg).

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

[![Smart-Traffic-Sensor Darknet integration](https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/docs/Darknet_integration.png)](https://www.youtube.com/watch?v=j7X3t8OMXaE&feature=youtu.be)


## Darknet
To train a model with my dataset I use ([Darknet](https://github.com/pjreddie/darknet)). I adapted it so I could install it on my computer and use DarknetApi on smart-traffic-sensor. I have this adaptation in https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez

If you have to use OpenCV, Cuda and GPU, you have to edit the Makefile:

```ruby
  GPU=0
  CUDNN=0
  OPENCV=0
```

To train you can execute make for generating the executable.

```ruby
  cd darknet
  make -j4
```
Here are the steps to follow to train a model with your dataset:

1- We need to generate the label files that Darknet uses. Darknet wants a .txt file for each image with a line for each ground truth object in the image that looks like:

```ruby
  <object-class> <x> <y> <width> <height>
```
Where x, y, width, and height are relative to the image's width and height. In my case I have xml label files because I used labelImg and I saved in this format.To generate these file(.txt) we will run the voc_label.py script in Darknet's scripts/ directory.
To execute this script you need a annotations folder (folder with xml labels), a .txt with the annotations names file (annotations_file.txt) and an output folder. 

Next it shows that it should contain the annotations_file.txt:

```ruby
0006-00000001.xml
0006-00000002.xml
0006-00000003.xml
0006-00000005.xml
0006-00000006.xml
0006-00000007.xml
0006-00000008.xml
...
```
You have to have the next files in the directory darknet/scripts:

![Directory](https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/docs/directory.png)

Now you can generate the .txt files (you get this files in output folder):
```ruby
   python voc_label.py -xml annotations/ -xml_files annotations_file.txt -out output/
```
