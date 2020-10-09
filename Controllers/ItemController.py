from flask import jsonify
import Services.ItemService as item
from Models import db, ma, item_schema, items_schema


def addItem(content):
    res = item.addItem(content)
    if res is not None:
        return item_schema.dump(res), 200
    else:
        return "INTERNAL SERVER ERROR", 500


def deleteItem(id):
    res = item.deleteItem(id)
    if res is not None:
        return item_schema.dump(res), 200
    else:
        return "INTERNAL SERVER ERROR", 500


def finishItem(id):
    res = item.finishItem(id)
    if res is not None:
        return item_schema.dump(res), 200
    else:
        return "INTERNAL SERVER ERROR", 500


def fetchFinishedList():
    res = item.fetchFinishedList()
    if res is not None:
        return items_schema.dump(res), 200
    else:
        return "INTERNAL SERVER ERROR", 500


def fetchUninishedList():
    res = item.fetchUnfinishedList()
    if res is not None:
        return items_schema.dump(res), 200
    else:
        return "INTERNAL SERVER ERROR", 500
