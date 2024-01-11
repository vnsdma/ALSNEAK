from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from main import Config
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
app = Flask(__name__)
migrate = Migrate(app, db)
app.config.from_object(Config)
db.init_app(app)
jwt = JWTManager(app)


from app.model import user,product,category_product
if __name__ == '__main__':
    app.run(debug=True)