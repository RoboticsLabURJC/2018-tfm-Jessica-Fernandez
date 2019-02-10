![Darknet Logo](http://pjreddie.com/media/files/darknet-black-small.png)

# Darknet #
Darknet is an open source neural network framework written in C and CUDA. It is fast, easy to install, and supports CPU and GPU computation.

For more information see the [Darknet project website](http://pjreddie.com/darknet).

For questions or issues please use the [Google Group](https://groups.google.com/forum/#!forum/darknet).

# Darknet Installation in the compputer#
I have used [Darknet] (https://pjreddie.com/darknet/) and I have adapted it so that we can use it in Jderobot with DarknetApi. You can install it following the instructions below:

```ruby
  Download https://github.com/RoboticsURJC-students/2018-tfm-Jessica-Fernandez/tree/master/darknet
  cd darknet
  mkdir build && cd build
For GPU users:
  cmake -DCMAKE_INSTALL_PREFIX=/usr/local -DUSE_GPU=ON ..
For CPU users:
  cmake -DCMAKE_INSTALL_PREFIX=/usr/local -DUSE_GPU=OFF ..
  
  make -j4
  sudo make -j4 install
```
