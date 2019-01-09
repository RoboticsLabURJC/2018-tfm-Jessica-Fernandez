//
// Created by frivas on 31/01/17.
//

#ifndef _DARKNET_MODEL_
#define _DARKNET_MODEL_

#include <DarknetAPI/DarknetAPI.h>
#include <boost/shared_ptr.hpp>
#include "FrameworkInferencer.h"

class DarknetModel: public FrameworkInferencer {
public:
    DarknetModel(const std::string& netConfig, const std::string& netWeights, const std::string& classNamesFile);
    Sample detectImp(const cv::Mat& image, double confidence_threshold);

private:
    std::string netConfig;
    std::string netWeights;
    boost::shared_ptr<DarknetAPI> cnn;
};


typedef boost::shared_ptr<DarknetModel> DarknetModelPtr;



#endif //_DARKNET_MODEL_
