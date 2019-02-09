# Install script for directory: /home/docker/Jessi/Darknet_combinado/darknet/src

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  if(EXISTS "$ENV{DESTDIR}/usr/local/lib/libdarknetLib.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/usr/local/lib/libdarknetLib.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}/usr/local/lib/libdarknetLib.so"
         RPATH "")
  endif()
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/lib/libdarknetLib.so")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/usr/local/lib" TYPE SHARED_LIBRARY FILES "/home/docker/Jessi/Darknet_combinado/darknet/build/src/libdarknetLib.so")
  if(EXISTS "$ENV{DESTDIR}/usr/local/lib/libdarknetLib.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/usr/local/lib/libdarknetLib.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}/usr/local/lib/libdarknetLib.so"
         OLD_RPATH "/usr/local/cuda/lib64:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}/usr/local/lib/libdarknetLib.so")
    endif()
  endif()
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/include/softmax_layer.h;/usr/local/include/reorg_layer.h;/usr/local/include/route_layer.h;/usr/local/include/image.h;/usr/local/include/crnn_layer.h;/usr/local/include/blas.h;/usr/local/include/matrix.h;/usr/local/include/connected_layer.h;/usr/local/include/region_layer.h;/usr/local/include/crop_layer.h;/usr/local/include/layer.h;/usr/local/include/demo.h;/usr/local/include/tree.h;/usr/local/include/lstm_layer.h;/usr/local/include/utils.h;/usr/local/include/normalization_layer.h;/usr/local/include/im2col.h;/usr/local/include/gru_layer.h;/usr/local/include/dropout_layer.h;/usr/local/include/parser.h;/usr/local/include/maxpool_layer.h;/usr/local/include/network.h;/usr/local/include/data.h;/usr/local/include/yolo_layer.h;/usr/local/include/cuda.h;/usr/local/include/stb_image.h;/usr/local/include/local_layer.h;/usr/local/include/list.h;/usr/local/include/activation_layer.h;/usr/local/include/box.h;/usr/local/include/convolutional_layer.h;/usr/local/include/deconvolutional_layer.h;/usr/local/include/gemm.h;/usr/local/include/rnn_layer.h;/usr/local/include/option_list.h;/usr/local/include/col2im.h;/usr/local/include/shortcut_layer.h;/usr/local/include/stb_image_write.h;/usr/local/include/detection_layer.h;/usr/local/include/avgpool_layer.h;/usr/local/include/batchnorm_layer.h;/usr/local/include/activations.h;/usr/local/include/classifier.h;/usr/local/include/cost_layer.h;/usr/local/include/upsample_layer.h")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/usr/local/include" TYPE FILE FILES
    "/home/docker/Jessi/Darknet_combinado/darknet/src/softmax_layer.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/reorg_layer.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/route_layer.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/image.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/crnn_layer.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/blas.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/matrix.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/connected_layer.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/region_layer.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/crop_layer.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/layer.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/demo.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/tree.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/lstm_layer.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/utils.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/normalization_layer.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/im2col.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/gru_layer.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/dropout_layer.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/parser.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/maxpool_layer.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/network.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/data.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/yolo_layer.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/cuda.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/stb_image.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/local_layer.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/list.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/activation_layer.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/box.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/convolutional_layer.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/deconvolutional_layer.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/gemm.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/rnn_layer.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/option_list.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/col2im.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/shortcut_layer.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/stb_image_write.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/detection_layer.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/avgpool_layer.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/batchnorm_layer.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/activations.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/classifier.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/cost_layer.h"
    "/home/docker/Jessi/Darknet_combinado/darknet/src/upsample_layer.h"
    )
endif()

