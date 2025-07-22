from PIL import Image
from io import BytesIO
import numpy as np
import utils.preprocess as pre
import requests
import certifi
import torch


def download_image(url: str) -> Image.Image:
    #相当于获得许可证
    ca_bundle_path = certifi.where()
    requests.get(url, verify = ca_bundle_path)

    """从URL下载图片并返回PIL图像对象"""
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # 检查请求是否成功
    img = Image.open(BytesIO(response.content)).convert('RGB')
    return img

#func：读照片进来并处理
def extract_vector_from_url(image_url: str) -> np.ndarray:
    """从URL提取特征向量"""
    try:
        img = download_image(image_url)
        x = pre.preprocess(img).unsqueeze(0)
        with torch.no_grad():
            feat = pre.feature_extractor(x).squeeze()
        vec = feat.cpu().numpy()
        vec /= (np.linalg.norm(vec) + 1e-6)
        return vec.astype('float32')
    except Exception as e:
        print(f"Error processing {image_url}: {e}")
        return None