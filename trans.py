import torch
from ultralytics import YOLO

# 加载 YOLOv8 官方的 .pt 模型
model = YOLO("model.pt")  # 替换为你需要的模型路径

# 将模型转换为 TorchScript 格式
model.export(format="torchscript")


torchscript_model = YOLO("model.torchscript")

# 保存为 TorchScript 文件
torchscript_model.save("model_torchscript.pt")
