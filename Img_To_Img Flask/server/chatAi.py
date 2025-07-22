from flask import jsonify
from openai import OpenAI

class ChatAI():
    def __init__(self, api_key):
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://api.moonshot.cn/v1",
        )

    def chat(self, data):
        place = data.get('place')

        if not place:
            return jsonify({"error": "缺少地标参数 place"}), 400

        history = [
            {"role": "system",
             "content": "你是一个专业的旅游讲解员。"}
        ]

        history.append({
            "role": "user",
            "content": f"你是一个旅游讲解员。请向用户介绍“{place}”这个地标，介绍包括其建筑风格、历史背景、使用用途等内容，语言简洁优美，控制在150字左右。"
        })

        try:
            completion = self.client.chat.completions.create(
                model="moonshot-v1-8k",
                messages=history,
                temperature=0.3,
            )
            result = completion.choices[0].message.content
            return jsonify({"message": result}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def get_description(self, place):
        """
        纯后端调用，传入地标名称，返回AI生成的介绍文本字符串
        """
        if not place:
            return "缺少地标参数 place"

        history = [
            {"role": "system",
             "content": "你是一个专业的旅游讲解员。"}
        ]

        history.append({
            "role": "user",
            "content": f"你是一个旅游讲解员。请向用户介绍“{place}”这个地标，介绍包括其建筑风格、历史背景、使用用途等内容，语言简洁优美，控制在150字左右。"
        })

        try:
            completion = self.client.chat.completions.create(
                model="moonshot-v1-8k",
                messages=history,
                temperature=0.3,
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"AI 讲解失败: {str(e)}"
