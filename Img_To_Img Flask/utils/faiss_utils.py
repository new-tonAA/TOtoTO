import numpy as np
from PIL import Image
import torch

# API需要的flask框架
import utils.preprocess as pre
import os

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

#func：读照片进来并处理
def extract_vector(image_path: object) -> any:
    img = Image.open(image_path).convert('RGB') # 打开图并转RGB
    x = pre.preprocess(img).unsqueeze(0)  # 对图像进行预处理，最终结果是[1,3,224,224]
    with torch.no_grad(): # 禁用梯度运算（为了快）
        feat = pre.feature_extractor(x).squeeze()  # 放进模型中并去除最后一层，结果为[2048]
    vec = feat.cpu().numpy() # 将张量从 GPU 移动到 CPU，并转换为 NumPy 数组（如果在GPU运行则是必要的）
    vec /= (np.linalg.norm(vec) + 1e-6)# 对特征向量进行 L2 归一化，分母即计算向量的欧几里得距离（防止分母为0才加的1e-6）
    return vec.astype('float32')# 返回了一个归一化的特征向量

def search_topk(query_path, index, paths, types, k=3): # k是返回结果数量（最接近的k个）
    qv = extract_vector(query_path) # 读照片进来处理
    D, I = index.search(np.expand_dims(qv, axis=0), k) # 在faiss索引中搜索最相似的k个向量（用欧几里得距离搜索）

    return [(types[i], paths[i], float(D[0][j])) for j, i in enumerate(I[0])] # 将faiss返回的索引位置和距离转换为具体的图像路径和数值