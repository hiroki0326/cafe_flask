from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'User'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text)
  email = db.Column(db.Text)
  age = db.Column(db.Text)
  reservation_date = db.Column(db.Date)
  reservation_time = db.Column(db.Time)

class Menu(db.Model):
  __tablename__ = 'Menu'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text)
  value = db.Column(db.Text)
  file_name = db.Column(db.Text)
  message = db.Column(db.Text)