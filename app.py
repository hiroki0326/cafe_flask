from flask import Flask
from flask_migrate import Migrate
from models import db

app = Flask(__name__, static_folder='static', static_url_path='/static')

# SQLAlchemy の設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# SQLAlchemy の初期化
db.init_app(app)
migrate = Migrate(app, db)

# controller import
from controllers.front import cafe, shop
from controllers.setting.cafe import reservation, menu

# shop
app.register_blueprint(shop.app)

# cafe
app.register_blueprint(cafe.app)

# setting cafe reservation
app.register_blueprint(reservation.app)

# setting cafe menu
app.register_blueprint(menu.app)

first_request = True

if first_request:
  with app.app_context():
    db.create_all()

if __name__ == '__main__':
  app.run(port=9999, debug=True)