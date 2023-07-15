from flask import Blueprint, render_template, request, redirect, url_for
from flask_paginate import Pagination, get_page_parameter
from datetime import datetime
from models import db, User

app = Blueprint('reservation', __name__)

@app.route('/setting/cafe/reservation/list')
def list():
  users = User.query.order_by(User.id.desc()).all()
  # ページネーション
  ## 現在のページ番号を取得
  page = int(request.args.get(get_page_parameter(), 1))
  ## ページごとの表示件数
  per_page = 10
  ## ページネーションオブジェクトを作成
  pagination = Pagination(page=page, per_page=per_page, total=len(users))
  # 表示するデータを取得
  start = (page - 1) * per_page
  end = start + per_page
  displayed_user = users[start:end]
  return render_template('setting/cafe/reservation/list.html', users=displayed_user, pagination=pagination)

@app.route('/setting/cafe/reservation/show/<int:user_id>')
def show(user_id):
  user = User.query.get(user_id)
  return render_template('setting/cafe/reservation/show.html', user=user)

# 新規保存
@app.route('/setting/cafe/reservation/create', methods=['POST'])
def create():
  reservation_date = datetime.strptime(request.form['reservation_date'], '%Y-%m-%d').date()
  reservation_time = datetime.strptime(request.form['reservation_time'], '%H:%M').time()
  user = User(name=request.form['name'], age=request.form['age'], email=request.form['email'], reservation_date=reservation_date, reservation_time=reservation_time)
  db.session.add(user)
  db.session.commit()
  return redirect('/setting/cafe/reservation/list')

# 編集機能
@app.route('/setting/cafe/reservation/edit/<int:user_id>')
def edit(user_id):
  user = User.query.get(user_id)
  return render_template('setting/cafe/reservation/edit.html', user=user)

# 保存
@app.route('/setting/cafe/reservation/save/<int:user_id>', methods=['POST'])
def save(user_id):
  user = User.query.get(user_id)
  if user:
    user.name = request.form['name']
    user.age = request.form['age']
    user.email = request.form['email']
    user.reservation_date = datetime.strptime(request.form['reservation_date'], '%Y-%m-%d').date()
    reservation_time = request.form['reservation_time'][:5]
    user.reservation_time = datetime.strptime(reservation_time, '%H:%M').time()
    db.session.commit()
  return redirect(url_for('reservation.show', user_id=user_id))

# 削除機能
@app.route('/setting/cafe/reservation/delete/<int:user_id>', methods=['GET', 'POST'])
def delete(user_id):
  user = User.query.get(user_id)
  if user:
    db.session.delete(user)
    db.session.commit()
  return redirect('/setting/cafe/reservation/list')