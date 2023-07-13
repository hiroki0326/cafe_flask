from flask import Blueprint, render_template, request, redirect
from datetime import datetime
from models import db, User, Menu

app = Blueprint('cafe', __name__)

@app.route('/cafe/')
def cafe():
  menus = Menu.query.all()
  return render_template('front/cafe/home.html', menus=menus)

@app.route('/cafe/list')
def list():
  users = User.query.all()
  return render_template('front/cafe/list.html', users=users)

# 新規保存
@app.route('/cafe/cafe-post', methods=['POST'])
def new_user():
  reservation_date = datetime.strptime(request.form['reservation_date'], '%Y-%m-%d').date()
  reservation_time = datetime.strptime(request.form['reservation_time'], '%H:%M').time()
  user = User(name=request.form['name'], age=request.form['age'], email=request.form['email'], reservation_date=reservation_date, reservation_time=reservation_time)
  db.session.add(user)
  db.session.commit()
  return render_template('front/cafe/show.html', user=user)

# 編集を保存
@app.route('/edit-user/<int:user_id>', methods=['POST'])
def edit_user(user_id):
  user = User.query.get(user_id)
  if user:
    user.name = request.form['name']
    user.age = request.form['age']
    user.email = request.form['email']
    user.reservation_date = datetime.strptime(request.form['reservation_date'], '%Y-%m-%d').date()
    user.reservation_time = datetime.strptime(request.form['reservation_time'], '%H:%M:%S').time()
    db.session.commit()
  return redirect('/cafe/list')

# 新規予約の編集を保存
@app.route('/new-edit/<int:user_id>', methods=['POST'])
def new_edit(user_id):
  user = User.query.get(user_id)
  if user:
    user.name = request.form['name']
    user.age = request.form['age']
    user.email = request.form['email']
    user.reservation_date = datetime.strptime(request.form['reservation_date'], '%Y-%m-%d').date()
    user.reservation_time = datetime.strptime(request.form['reservation_time'], '%H:%M:%S').time()
    db.session.commit()
  return render_template('front/cafe/show.html', user=user)

# 削除機能
@app.route('/delete/<int:user_id>', methods=['GET', 'POST'])
def delete_user(user_id):
  user = User.query.get(user_id)
  if user:
    db.session.delete(user)
    db.session.commit()
  return redirect('/cafe/list')

# 新規予約の削除機能
@app.route('/new-delete/<int:user_id>', methods=['GET', 'POST'])
def new_delete(user_id):
  user = User.query.get(user_id)
  if user:
    db.session.delete(user)
    db.session.commit()
  return redirect('/cafe/')