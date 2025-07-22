from torchvision import models, transforms
from torchvision.models import resnet50, ResNet50_Weights
import torch.nn as nn

# 1.模型
# 方式 A：预训练权重
#model = models.resnet50(weights=True).eval()# 定义resnet50模型，这是pytorch中的一个模型库
# 其中ResNet-50 是一个经典的深度卷积神经网络，有 50 层深度，常用于图像分类任务
# 或者 方式 B：显式指定权重（需 torchvision >= 0.13）
model = models.resnet50(weights=ResNet50_Weights.IMAGENET1K_V1).eval()

# 将模型（如 ResNet-50）的最后一层移除，并用剩余部分构建一个新的特征提取器feature_extractor
feature_extractor = nn.Sequential(*list(model.children())[:-1])
# 原始模型（如 ResNet-50）最后一层通常是全连接层（nn.Linear），用于分类任务。移除后，模型仅保留特征提取部分。

# 2.预处理：定义一个预处理流程（此时不会执行任何操作），实际使用时才会执行预处理
preprocess = transforms.Compose([ # 对所有图像进行统一处理
    transforms.Resize(256),# 将图像的短边缩放到 256 像素，长边按比例缩放，保持图像宽高比不变。
    transforms.CenterCrop(224), # 从图像中心裁剪出一个 224x224 像素的正方形区域（能否改进？例如保留更大的区域）
    transforms.ToTensor(), # 将数据转化为pytorch格式可用
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]), # 归一化 即对每个像素值先减去均值mean，再除以标准差std
    # 归一化目的：将数据分布调整到均值为0、标准差为1的标准正态分布，加速模型收敛并提升性能。
])