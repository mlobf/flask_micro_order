from flask import Flask, request
from flask_migrate import Migrate
from models import db, init_app
import os
from routes import order_blueprint


app = Flask(__name__)

file_path = os.path.abspath(os.getcwd()) + "/database/user.db"


app.config["SECRET_KEY"] = "JTEsEs7a6LK72-mIrOlsWMxaaxrlFCmFbG"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + file_path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

init_app(app)
app.register_blueprint(order_blueprint)
# migrate = Migrate(app, models.db)


if __name__ == "__main__":
    app.run(debug=True, port=5003)
