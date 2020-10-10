from flask import Flask, request
from Models import db, ma
from config import Config
from route import ItemBlueprint

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
ma.init_app(app)
app.register_blueprint(ItemBlueprint)

if __name__ == "__main__":
    app.run()
