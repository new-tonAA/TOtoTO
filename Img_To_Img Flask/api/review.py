#评论区
from flask import Blueprint, request, jsonify, session
from model.models import db, Review, User
from datetime import datetime

review_api = Blueprint('review_api', __name__, url_prefix='/review')

@review_api.route('', methods=['POST'])
def add_review():

    data = request.get_json()
    comment = data.get('comment')
    print(f"收到的数据: {data}")

    if not comment:
        return jsonify({'error': '评论内容不能为空'}), 400

    review = Review(
        comment=comment.strip(),
        create_time=datetime.utcnow(),
        update_time=datetime.utcnow()
    )
    try:
        db.session.add(review)
        db.session.commit()
        return jsonify({'message': '评论成功', 'id': review.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'数据库写入失败: {str(e)}'}), 500

@review_api.route('/list', methods=['GET'])
def list_reviews():
    reviews = Review.query.order_by(Review.create_time.desc()).limit(45).all()
    resp = []
    for r in reviews:
        resp.append({
            'id': r.id,
            'comment': r.comment,
            'create_time': r.create_time.isoformat(timespec="seconds")
        })
    return jsonify(resp), 200
