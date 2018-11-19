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
![Keras example](https://youtu.be/0MeZSVHg-3M)
