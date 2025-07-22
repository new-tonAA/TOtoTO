from model.models import Record as modelsRecord
from model.models import db

class Record():
    def findByUserId(userId):
        records=modelsRecord.query.filter_by(create_user = userId).all()
        return records;

    def findByRecordId(recordId):
        record = modelsRecord.query.filter_by(id = recordId).first()
        return record

    def add_record(record):
        db.session.add(record)
        db.session.commit()
        return record