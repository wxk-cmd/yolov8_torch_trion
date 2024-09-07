# Overview
This repository provides an ensemble model to combine a YoloV8 model exported from the Ultralytics repository with NMS post-processing.The NMS post-processing code contained in yolov8_onnx.py is adapted from the Ultralytics ONNX Example.

# Directory Structure
    models/
      yolov8_torch/
          1/
              model.pt
          config.pbtxt
  
    README.md
    bus.jpg
    yolov8_torch.py
    trans.py
# Quick Start
1.Install Ultralytics 
    ```pip install ultralytics```   
2.Export pt format to torchscript model:  
    ```python trans.py```     
3.Rename the model file to and place it under the directory (see directory structure above).```model.pt /models/yolov8_torch/1```      
4.(Optional): Update the Score and NMS threshold in ```yolov8_torch.py```     
5.(Optional): Update the models/yolov8_torch/config.pbtxt file if your input resolution has changed     
6.Run Triton Inference Server:      
    ```docker run --gpus=1 --rm --net=host -v ${PWD}/model_repository:/models nvcr.io/nvidia/tritonserver:24.07-py3 tritonserver --model-repository=/models```       
7.Run Triton Inference client(install opencv-python before run):     
    ```python yolov8_torch.py```      
