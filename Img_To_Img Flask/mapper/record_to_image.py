from model.models import RecordToImage as modelsRecordToImage
from model.models import db

class RecordToImage:  #以connection来命名
    def add_connection(connection):
        db.session.add(connection)
        db.session.commit()
        return connection.id

    def findByrecordId(hid):
        connection = modelsRecordToImage.query.filter_by(record_id=hid).all()
        return connection