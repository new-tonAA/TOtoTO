from werkzeug.utils import secure_filename
import datetime
import requests
import certifi
import re
import base64

def get_url(image,local):
    url_content = image.read()  # 读取 .url 文件内容

    if image.filename.lower().endswith('.url'):
        try:
            url_content = url_content.decode('utf-8')
        except UnicodeError:
            url_content = url_content.decode('latin-1')

        # 2. 提取 URL（正则匹配）
        url_match = re.search(r'URL=(https?://[^\s]+)', url_content)
        if not url_match:
            raise ValueError("无效的 .url 文件，未找到有效 URL")
        image_url = url_match.group(1)

        # 3. 下载图片
        response = requests.get(image_url)
        if response.status_code != 200:
            raise ValueError("图片下载失败")

        # 3. 读取文件内容并转为 Base64
        image_data = response.content  # 获取图片二进制数据
        base64_data = base64.b64encode(image_data).decode('ascii')  # 转为 Base64 字符串
    else:
        base64_data= base64.b64encode(url_content).decode('ascii')

    # 获取安全的文件名并提取扩展名
    original_filename = secure_filename(image.filename)
    match = re.search(r"\.(jpg|png|gif|bmp|webp)(?=\.url$)", original_filename, re.IGNORECASE)

    if match:
        img_ext = "." + match.group(1)  # 提取 .png 并加上前面的点
    else:
        img_ext = ".jpg"  # 默认后缀（如果未匹配到）

    token =   # 自行去github生成token
    curr_time = datetime.datetime.now()
    path = curr_time.strftime("%Y%m%d%H%M%S") + img_ext
    url = #f"https://api.github.com/repos/new-tonAA/Images/contents/{local}/" + path # 用户名、库名、路径
    headers = {
        "Authorization": "token " + token,
    }
    content = base64_data;
    data = {
        "message": "zj upload pictures",
        "content": content
    }

    try:
        # 相当于获得许可证
        ca_bundle_path = certifi.where()
        response = requests.put(url=url, json=data, headers=headers, verify=ca_bundle_path)

        # Check if request was successful
        if response.status_code == 201:
            print("File uploaded successfully!")
            img = #f"https://raw.githubusercontent.com/new-tonAA/Images/refs/heads/main/{local}/{path}"
            print(img)
            return img
        else:
            print(f"Error uploading file: {response.status_code} - {response.text}")
            return None

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
