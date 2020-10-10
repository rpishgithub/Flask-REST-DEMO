from Models import db
from Models.Item import Item

# from Services.ItemService import initDB


def initDB():
    from flask import Flask
    from Models import db
    from config import Config
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        db.create_all()


def addItem(content):
    item = Item(content)
    db.session.add(item)
    db.session.commit()
    return item


def searchItem(id):
    item = Item.query.filter_by(id=id).first()
    return item


def deleteItem(id):
    item = searchItem(id)
    db.session.delete(item)
    db.session.commit()
    return item


def finishItem(id):
    item = searchItem(id)
    item.isFinished = True
    db.session.commit()
    return item


def fetchUnfinishedList():
    items = Item.query.filter_by(isFinished=False).all()
    return items


def fetchFinishedList():
    items = Item.query.filter_by(isFinished=True).all()
    return items
