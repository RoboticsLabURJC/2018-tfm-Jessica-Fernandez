---
layout: default
---
# Autoevaluator- dl-DetectionSuite



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
