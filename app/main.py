from flask import Flask
from flask_restful import Api
from app.extensions import db, ma
from app.models.all_models import *
from app.settings import DATABASE_URI
from app.routes import routes


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLAlCHEMY_TRACK_NOTIFICATIONS'] = False
# app.config['JWT_SECRET_KEY'] = "MY SECRET KEY"
app.config.from_pyfile('settings.py')

api = Api(app)

routes(api)

@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    app.run(port=8000, host='127.0.0.1', debug=True)
