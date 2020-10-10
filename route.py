from flask import Blueprint, request
import Controllers.ItemController as ItemController

ItemBlueprint = Blueprint('ItemBlueprint', __name__, url_prefix='/todo')


@ItemBlueprint.route('/add', methods=['POST'])
def addItemAPI():
    content = request.form.get('content')
    res = ItemController.addItem(content)
    return res


@ItemBlueprint.route('/delete/<id>', methods=['GET'])
def deleteItemAPI(id):
    res = ItemController.deleteItem(id)
    return res


@ItemBlueprint.route('/finish/<id>', methods=['GET'])
def finishItemAPI(id):
    res = ItemController.finishItem(id)
    return res


@ItemBlueprint.route('/unfinished', methods=['GET'])
def fetchUnfinishedListAPI():
    res = ItemController.fetchUnfinishedList()
    return res


@ItemBlueprint.route('/finished', methods=['GET'])
def fetchFinishedListAPI():
    res = ItemController.fetchFinishedList()
    return res
