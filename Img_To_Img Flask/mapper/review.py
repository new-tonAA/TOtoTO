# mapper/review.py
from model.models import Review as modelsReview
from model.models import db

class Review:

    def add_review(self, review_obj: modelsReview):
        """写入一条评论，返回主键 ID"""
        db.session.add(review_obj)
        db.session.commit()
        return review_obj.id

    def list_latest(self, limit=50, offset=0):
        """按时间倒序获取评论列表"""
        return (modelsReview.query
                .order_by(modelsReview.create_time.desc())
                .offset(offset)
                .limit(limit)
                .all())
