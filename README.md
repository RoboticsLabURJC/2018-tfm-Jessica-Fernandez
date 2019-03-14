# 2018-tfm-Jessica-Fernandez
## Autoevaluator- dl-DetectionSuite. Test 1
I used ([dl-DetectionSuite](https://github.com/JdeRobot/dl-DetectionSuite)) to compare the different model that I have. In this ocasion I haven't had the far cars in account. Also I have evaluated the pretrained networks that I used to do the training. With this condition I got the next results:

|        Network        |  mAP(Overall)(IOU=0.5:0.95) | mAR(Overall)(IOU=0.5:0.95) | Mean inference time (ms) | 
| --------------------- | --------------------------- | -------------------------- | ------------------------ |
|          Keras        |           0.617666	      |          0.653703          |           3427           | 
|          Yolo         |           0.56836	      |          0.615658          |           16894          |
|       Tensorflow      |           0.454884	      |          0.490377          |            76            |  
|    Keras-Pretrained   |              0	      |              0             |             0            | 
|    Yolo-Pretrained    |              0	      |              0             |           14162          |
| Tensorflow-Pretrained |           0.0141532	      |          0.0398529         |            142           |  

## Tensorflow - Smart traffic sensor
In the original smart-traffic-sensor, tensorflow is implemented in C++. When I trained my own database I used ([tensorflow/models](https://github.com/tensorflow/models)). tensorflow/models has been updated and it's incompatible wwith the tensorflow implementation in smart-traffic-sensor, because in this case an older version of tensorflow was used.
For this reason I have put tensorflow in python. Because if in the future tensorflow / models is updated again, we would be limited to the version that we place in smart-traffic-sensor. With Python we avoid this problem, since it is only necessary to update tensorflow in the computer.

In the next video you can see tensorflow in smart-traffic-sensor:

[![Smart-Traffic-Sensor Tensorflow1](https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/docs/tensorflow_smart_traffic_sensor.png)](https://www.youtube.com/watch?v=AyDBIZC3P2A&feature=youtu.be)

## Autoevaluator- dl-DetectionSuite
I used ([dl-DetectionSuite](https://github.com/JdeRobot/dl-DetectionSuite)) to compare the different model that I have.To use dl-DetectionSuite you have to install it as explained on it github. In particular you should use Tools/Autoevaluator. First, you need a images folder, a annotations folder and a .yml file:

```ruby
Datasets:

-
  inputPath: /home/vanejessi/dl-DetectionSuite/DeepLearningSuite/build/Tools/AutoEvaluator/annotations
  readerImplementation: ImageNet
  readerNames: /home/vanejessi/dl-DetectionSuite/DeepLearningSuite/build/Tools/AutoEvaluator/names/label.names


Inferencers:

-
  inferencerWeights:         /opt/datasets/weights/ssd300adam_1000_cambio_ancho_coco_120_inference.h5
  inferencerConfig:          /opt/datasets/cfg/foo.cfg             
  inferencerImplementation:  keras                                 
  inferencerNames:           /home/vanejessi/dl-DetectionSuite/DeepLearningSuite/build/Tools/AutoEvaluator/names/label.names
  iouType:                   bbox                                             

-

  inferencerWeights:         /home/vanejessi/dl-DetectionSuite/DeepLearningSuite/build/Tools/AutoEvaluator/weights/yolov3-voc_17000.weights
  inferencerConfig:          /opt/datasets/cfg/yolov3-voc.cfg       
  inferencerImplementation:  yolo                                  
  inferencerNames:           /home/vanejessi/dl-DetectionSuite/DeepLearningSuite/build/Tools/AutoEvaluator/names/label_yolo.names
  iouType:                   bbox                                          

-
  inferencerWeights:         /home/vanejessi/dl-DetectionSuite/DeepLearningSuite/build/Tools/AutoEvaluator/weights/frozen_inference_graph.pb
  inferencerConfig:          /opt/datasets/cfg/foo.cfg              
  inferencerImplementation:  tensorflow                             
  inferencerNames:           /home/vanejessi/dl-DetectionSuite/DeepLearningSuite/build/Tools/AutoEvaluator/names/labels.pbtxt
  iouType:		     bbox


outputCSVPath: /home/vanejessi/dl-DetectionSuite/DeepLearningSuite/build/Tools/AutoEvaluator/output
```

For executing you have to go to /dl-DetectionSuite/DeepLearningSuite/build/Tools/AutoEvaluator and you should execute:

```ruby
./autoEvaluator -c appConfig.yml
```

I have compared my three model (Keras, Yolo and Tensorflow) and I got:

| Network    |  mAP(Overall)(IOU=0.5:0.95) | mAR(Overall)(IOU=0.5:0.95) | Mean inference time (ms) |
| -----------| --------------------------- | -------------------------- | ------------------------ |
| Keras      |           0.459113	   |          0.502304          |           3194           |
| Yolo       |           0.502507	   |          0.580324          |           15357          |
| Tensorflow |           0.308906	   |          0.360332          |            83            |
 	 

## Tensorflow model in Smart-traffic-sensor
I tried my tensorflow model in the smart-traffic-sensor and I got the next result:

[![Smart-Traffic-Sensor Tensorflow](https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/docs/tensorflow_model.png)](https://www.youtube.com/watch?v=-QbA6TPE2ds&feature=youtu.be)

## Tensorflow Training
I have trained a tensorflow model with my own database. The steps to train are indicated below:
1. Download tensorflow models:
```ruby
git clone https://github.com/tensorflow/models
```
2. Prepare your training data

For this you can reuse some already existing database or generate your own data. To train
the vehicles-detection module of traffic monitor I generated my own database of vehicles
following the PASCAL VOC format. This is a well-known format that can be used later to generate
the traing.record and testing.record TFRecord files needed by tensorflow to re-train an already
existing network.

To generate the TFRecords a modified version of create_pascal_tf_record.py script will be used. Basically,
the original script provided by tensorflow is ready to receive as input a dataset in PASCAL VOC format directory
structure and use it to generate the TF records. However, the PASCAL structure is too complicated
for what's needed, so a modified script will be used so it can handle the following directory structure:

```
 dataset \
         \-- annotations
         \-- images
         \-- files.txt
         \-- labels.pbtxt
```

Where:
* annotations   : directory containing the XML annotations
* images        : directory containing the JPEG images
* files.txt     : a file listing the images to be used for training
* labels.pbtxt  : file containg the classes labels

The file **labels.pbtxt** must contain a list of the object classes, i.e:

```
item {
  id: 1
  name: "car"
}
item {
  id: 2
  name: "motorcycle"
}
...
```

Once the data is ready you can create the **test.record** and **traing.cord** as following:

```
   python machine-learning/tools/create_pascal_tf_record.py --data_dir vehicles-dataset/ --output_path data/test.record --files test-files-balanced.txt 
```

3. Re-training the network

  Before starting the re-training script, you have to decide which network you will be using as starting point.
  There are several pre-trained networks in [tensorflow zoo model][1] repository, just pick one that fullfill your
  needs. Since in my case I'm looking for a fast object detection network, my first choice is SSD mobilenet V2
  network. This network provides a good tradeoff between accurracy and speed. Once you decice which network to
  use, you have to download its **.pb** file and configuration file. In the case of SSD mobilenet V2 you can get
  the configuration file from the following [link][2]. This file contains severaltraining parametres needed
  by this network, but you just need to fine-tune some of them, for instance:

   * **num_classes**: as its name indicate, this parameter indicates the number of classes
   * **input_path** (tf_record_input_reader record): this parameter must point to the train.record file generated previously
   * **label_map_path** (tf_record_input_reader record): this parameter must point to the labels.pbtxt file generated previously

  For example in my setup, the configuration file looks like:

```
train_input_reader: {
  tf_record_input_reader {
    input_path: "data/train.record"
  }
  label_map_path: "data/labels.pbtxt"
}
```

   The same must be done for the testing records, pointing to the right files. At this point you have all what you need to start the
   re-training script. My data directory structure is as following:

```
 data \
      \-- labels.pbtxt
      \-- ssd_mobilenet_v2_coco.config
      \-- test.record
      \-- train.record
```

   To launch the re-training you have to:

   1. Go to the directory models/research/object_detection/legacy
   2. Copy the data directory to hold the files needed for training (see above)
   3. Copy the images directory to the local directory
   4. In models/research, you have to execute: protoc object_detection/protos/*.proto --python_out=.
   5. Launch the training script as following:

```bash
   export PYTHONPATH=../..:../../slim/
   python train.py --logtostderr --train_dir training/ --pipeline_config_path=./data/ssd_mobilenet_v2_coco.config
```

   This will start the training process that may last for a while. During the same you can monitor the loss-function
   so you can stop it whenever it reaches a reasonable value. By default it will stop automatically after 200k steps.
   The training script from time to time saves a checkpoint (you can see them at training_dir/checkpoint).


3. Generate your model

   At this point you have already ran the training script and generated our model, but the results are still in the intermediate
   format. In order to use the generated model outside you have to freeze it to a **.pb** network graph file. For this you have to
   use the export_inference_graph.py script (from legacy directory):

```bash
python ../export_inference_graph.py --input_type image_tensor --pipeline_config_path data/ssd_mobilenet_v2_coco.config --trained_checkpoint_prefix training/model.ckpt-XXX --output_directory mymodel/
```

  where XXX are digits corresponding to the checkpoint to be used.

  Finally, this generates a new directory **mymodl** where the **.pb** plus other model data are saved.
## Darknet - Smart-traffic-sensor

I tried my trained Darknet model with smart-traffic-sensor and I got the next result:

[![Smart-Traffic-Sensor Darknet integration1](https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/docs/Darknet.png)](https://www.youtube.com/watch?v=BBAZv2HKhWM)

After this, I adapted to vehicle model of smart-traffic-sensor.You can see the result in the following video:

[![Smart-Traffic-Sensor Darknet](https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/docs/Darknet_smart-traffic-sensor.png)](https://www.youtube.com/watch?v=6bPlBcT80W4)


## Darknet Training
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
To execute this script you need an annotations folder (folder with xml labels), a .txt with the annotations names file (annotations_file.txt) and an output folder. 

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
   python voc_label.py -xml annotations/ -xml_files annotations_file.txt -out labels/
```
You have to copy the labels folder in the darknet/data folder. In the arknet/folder you should have the images and labels folders.

2- Darknet needs one text file with all of the images you want to train on and other with all of the images you want to test. Below is an example of what you should put in both files:

```ruby
   /home/docker/Jessi/Darknet_training/darknet/data/images/0081-00000055.jpg
   /home/docker/Jessi/Darknet_training/darknet/data/images/0081-00000056.jpg
   /home/docker/Jessi/Darknet_training/darknet/data/images/0081-00000057.jpg
   /home/docker/Jessi/Darknet_training/darknet/data/images/0081-00000058.jpg
   /home/docker/Jessi/Darknet_training/darknet/data/images/0081-00000059.jpg
   /home/docker/Jessi/Darknet_training/darknet/data/images/0081-00000060.jpg
```
In my case I have these files in scripts folder.

3- We have to change the cfg/voc.data config file to point to your data:

```ruby
   classes= 8
   train  = /home/docker/Jessi/Darknet_training/darknet/scripts/train.txt
   valid  = /home/docker/Jessi/Darknet_training/darknet/scripts/test.txt
   names = /home/docker/Jessi/Darknet_training/darknet/data/voc.names
   backup = /home/docker/Jessi/Darknet_training/darknet/backup
```
voc.names is a file where the names of the classes that we want to train are indicated. backup is a folder where all the results will be saved. The weights file are saved very 100 iterations during the first 1000 iterations and then every 1000 iterations.  If you need change this you have to edit the line 138 of examples/detector.c (if(i%1000==0 || (i < 1000 && i%100 == 0))).

My voc.names is the next:

```ruby
   None
   motorcycle
   car
   van
   bus
   truck
   small-truck
   tank-truck
```

4- For training we use convolutional weights that are pre-trained on Imagenet. We use weights from the darknet53 model. You can just download the weights for the convolutional layers [here (76 MB)](https://pjreddie.com/media/files/darknet53.conv.74).

5- You have to edit the .cfg file. In my case I used yolov3-voc.cfg. You must modify the following:
 * change line batch to [`batch=64`](https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/darknet/cfg/yolov3-voc.cfg#L6)
  * change line subdivisions to [`subdivisions=16`](https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/darknet/cfg/yolov3-voc.cfg#L7)
  * change line `classes=8` to your number of objects in each of 3 `[yolo]`-layers:
      * https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/darknet/cfg/yolov3-voc.cfg#L611
      * https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/darknet/cfg/yolov3-voc.cfg#L695
      * https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/darknet/cfg/yolov3-voc.cfg#L779
  * change [`filters=39`] to filters=(classes + 5)x3 in the 3 `[convolutional]` before each `[yolo]` layer
      * https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/darknet/cfg/yolov3-voc.cfg#L605
      * https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/darknet/cfg/yolov3-voc.cfg#L689
      * https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/darknet/cfg/yolov3-voc.cfg#L773

  So if `classes=1` then should be `filters=18`. If `classes=2` then write `filters=21`.
  * you need to calculate the anchors. For it,  you have to execute gen_anchor.py:
      ```ruby
  	 python gen_anchor.py -filelist train.txt -output_dir anchors -num_clusters 9
      ```
      You will get the anchors.txt in the anchors folder.With it, you have to change line `anchors` in each of 3 `[yolo]`
      layers:
      * https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/darknet/cfg/yolov3-voc.cfg#L610
      * https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/darknet/cfg/yolov3-voc.cfg#L694
      * https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/darknet/cfg/yolov3-voc.cfg#L778

6- Now we can train! Run the command:

```ruby
./darknet detector train cfg/voc.data cfg/yolov3-voc.cfg darknet53.conv.74
```

During training, you will see varying indicators of error, and you should stop when no longer decreases 0.XXXXXXX avg:

```ruby
Region Avg IOU: 0.798363, Class: 0.893232, Obj: 0.700808, No Obj: 0.004567, Avg Recall: 1.000000, count: 8 Region Avg IOU: 0.800677, Class: 0.892181, Obj: 0.701590, No Obj: 0.004574, Avg Recall: 1.000000, count: 8

9002: 0.211667, 0.060730 avg, 0.001000 rate, 3.868000 seconds, 576128 images Loaded: 0.000000 seconds
```

* 9002 - iteration number (number of batch)
* 0.060730 avg - average loss (error) - the lower, the better

When you see that average loss 0.xxxxxx avg no longer decreases at many iterations then you should stop training.

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

## Smart-traffic-sensor Keras
I tested my keras model ( the 5º test) on the smart-traffic-sensor.Below you can see a video:

[![Smart-Traffic-Sensor Keras](https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/docs/smart_traffic_sensor_keras.png)](https://www.youtube.com/watch?v=pa6c3zmug8w&feature=youtu.be)


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

## Week 2
I'm labelling some traffic images for creating a database. For this, I use [labelImg](https://github.com/tzutalin/labelImg).

![labelImg](https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/docs/Captura%20de%20pantalla%20de%202018-11-03%2014-29-36.png)

## Week 1
To start I downloaded the component [Object Detector](https://github.com/JdeRobot/dl-objectdetector). In this component, you can upload the model of your neural network and the captured image of a webcam or video to test how your neural network works. In mi case I used a ssdlite_mobilenet_v2_coco_2018_05_29.pb model and a traffic video. In the next image you can see an example:

![Object_detector](https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/blob/master/docs/Captura%20de%20pantalla%20de%202018-10-12%2018-26-54.png)
