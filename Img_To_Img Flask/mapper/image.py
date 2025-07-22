from model.models import Image as modelsImage
from model.models import db

class Image():
    @staticmethod
    def add_image(image):
        db.session.add(image)
        db.session.commit()
        return {'添加成功'}

    @staticmethod
    def get_image(excludeId=[]):
        images = modelsImage.query.filter(modelsImage.id.notin_(excludeId)).all()
        return images

    @staticmethod
    def find_imageUrlById(imageId):
        img = modelsImage.query.filter_by(id=imageId).first()
        if img is None:
            return None
        else:
            return img.image

    @staticmethod
    def findById(imageId):
        return modelsImage.query.filter_by(id=imageId).first()

