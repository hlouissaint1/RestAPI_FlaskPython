__author__ = "Himmler Louissaint"
from Web_Development.Web_Tutorial_SQLAchemy.db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    items = db.relationship('ItemModel')
#    items = db.relationship('ItemModel', lazy='dynamic')


    def __init__(self, name):
        self.name = name

    def json(self):
 #       return {'name': self.name, 'items': [item.json() for item in self.items.all()]}
        return {'name': self.name, 'items': [item.json() for item in self.items]}

    def __str__(cls):
        return f"StoreModel(name={cls.name}"

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.commit()


if __name__ == '__main__':
    name = 'piano'
    print(StoreModel.find_by_name(name))