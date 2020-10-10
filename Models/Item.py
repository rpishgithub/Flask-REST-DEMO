from . import db, ma


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    isFinished = db.Column(db.Boolean, nullable=False)

    def __init__(self, content, isFinished=False):
        self.content = content
        self.isFinished = isFinished


class ItemSchema(ma.Schema):
    class Meta:
        fields = ("id", "content", "isFinished")


item_schema = ItemSchema()
items_schema = ItemSchema(many=True)
