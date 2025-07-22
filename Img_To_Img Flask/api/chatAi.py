from flask import Blueprint, jsonify, request
from server.chatAi import ChatAI
chatai_api = Blueprint('chatai_api', __name__)

guide_ai = ChatAI(api_key = #your api token)

@chatai_api.route('/chat', methods=['GET'])
def query():
    data = request.args.to_dict()
    return guide_ai.chat(data = data)