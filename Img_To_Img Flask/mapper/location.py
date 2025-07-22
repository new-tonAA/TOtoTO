# 访问数据库根据编号查找经纬度/获得地理名称
class Location:
    @staticmethod
    def findByType(category_id):
        from model.models import ImageCategory as CategoryModel
        return CategoryModel.query.filter_by(id=category_id).first()

    @staticmethod
    def findTypeNameByType(type):
        from model.models import ImageCategory as CategoryModel
        category = CategoryModel.query.filter_by(id=type).first()
        if category:
            return category.name
        return None





