---
layout: default
---
# Neuronal Network with Keras

I have been looking for neuronal networks with keras for objects detection. Currently the ssd networks are having great success, so I've tried these networks. For this I have based on: https://github.com/pierluigiferrari/ssd_keras . I did some tests.

## 1º Test
I tried the ssd300 with 1000 steps per epochs, 70 epochs and adam. I used the parameters, which are in the ssd300 example and I get the next result:

[![Smart-Traffic-Sensor With SSD300 Keras. First Example](https://roboticsurjc-students.github.io/2018-tfm-Jessica-Fernandez/images/keras1.png)](https://www.youtube.com/watch?v=qZrhYQ3WXGc&feature=youtu.be)

## 2º Test
I tried the ssd300 with 1000 steps per epochs, 120 epochs and SGD. I used the parameters, which are in the ssd300 example and I get the next result:

[![Smart-Traffic-Sensor With SSD300 Keras. Second Example](https://roboticsurjc-students.github.io/2018-tfm-Jessica-Fernandez/images/keras2.png)](https://www.youtube.com/watch?v=nEIczwMrbWc&feature=youtu.be)

## 3º Test
I tried the ssd7 with 1000 steps per epochs, 20 epochs and Adam. I used the parameters, which are in the ssd7 example and I get the next result:

[![Smart-Traffic-Sensor With SSD7 Keras. Example](https://roboticsurjc-students.github.io/2018-tfm-Jessica-Fernandez/images/keras3.png)](https://www.youtube.com/watch?v=71yQjBs76Vo&feature=youtu.be)

## 4º Test
I tried the ssd300 with 1000 steps per epochs, 70 epochs and Adam. In this case the steps parameter is None, the offsets parameter is None and I used the coco scales.

[![Smart-Traffic-Sensor With SSD300 Keras.Third Example](https://roboticsurjc-students.github.io/2018-tfm-Jessica-Fernandez/images/keras4.png)](https://www.youtube.com/watch?v=zGyK0PKNP7I&feature=youtu.be)

## 5º Test
I tried the ssd300 with 1000 steps per epochs, 120 epochs and Adam. In this case the steps parameter is None, the offsets parameter is None and I used the coco scales.

[![Smart-Traffic-Sensor With SSD300 Keras.Four Example](https://roboticsurjc-students.github.io/2018-tfm-Jessica-Fernandez/images/keras5.png)](https://www.youtube.com/watch?v=-tzJgebQSmw&feature=youtu.be)


