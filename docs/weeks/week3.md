---
layout: default
---
# Week 3


I have been integrating keras in smart-traffic-sensor. For this, I have to embeded Python code in C++. You can find information in the following links: [https://docs.python.org/2/extending/embedding.html] , [https://realmike.org/blog/2012/07/05/supercharging-c-code-with-embedded-python/] , [https://www.codeproject.com/Articles/11805/Embedding-Python-in-C-C-Part-I]. You can see a basic example in the next code (hello_python.cpp):
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

[![Smart-Traffic-Sensor With Keras. First Example](https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/docs/images/Captura%20de%20pantalla%20de%202018-11-19%2022-35-38.png)](https://www.youtube.com/watch?v=0MeZSVHg-3M)
