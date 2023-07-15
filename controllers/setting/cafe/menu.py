from flask import Blueprint, render_template,request, redirect, url_for
from flask_paginate import Pagination, get_page_parameter
from models import db, Menu
from datetime import datetime
import os

app = Blueprint('menu', __name__)

@app.route('/setting/cafe/menu/list')
def list():
  menus = Menu.query.order_by(Menu.id.desc()).all()
  # ページネーション
  ## 現在のページ番号を取得
  page = int(request.args.get(get_page_parameter(), 1))
  ## ページごとの表示件数
  per_page = 10
  ## ページネーションオブジェクトを作成
  pagination = Pagination(page=page, per_page=per_page, total=len(menus))
  # 表示するデータを取得
  start = (page - 1) * per_page
  end = start + per_page
  displayed_menu = menus[start:end]
  return render_template('setting/cafe/menu/list.html', menus=displayed_menu, pagination=pagination)

@app.route('/setting/cafe/menu/show/<int:menu_id>')
def show(menu_id):
  menu = Menu.query.get(menu_id)
  return render_template('setting/cafe/menu/show.html', menu=menu)

# 新規保存
@app.route('/setting/cafe/menu/create', methods=['POST'])
def create():
  # 画像の保存
  file = request.files['image']
  #file名の作成
  now = datetime.now()
  current_time = now.strftime("%Y-%m-%d%H:%M")
  new_file_name = f"{current_time}{file.filename}"
  file.save(os.path.join('./static/images/menus', new_file_name))
  menu = Menu(name=request.form['name'], value=request.form['value'], message=request.form['message'])
  menu.file_name = new_file_name
  db.session.add(menu)
  db.session.commit()
  return redirect('/setting/cafe/menu/list')

# 編集機能
@app.route('/setting/cafe/menu/edit/<int:menu_id>')
def edit(menu_id):
  menu = Menu.query.get(menu_id)
  return render_template('setting/cafe/menu/edit.html', menu=menu)

# 編集保存
@app.route('/setting/cafe/menu/save/<int:menu_id>', methods=['POST'])
def save(menu_id):
  menu = Menu.query.get(menu_id)
  if menu:
    if menu.file_name and request.files['image']=='':
      os.remove('./static/images/menus/' + menu.file_name)
    menu.name = request.form['name']
    menu.value = request.form['value']
    menu.message = request.form['message']
    if request.files['image']:
      file = request.files['image']
      #file名の作成
      now = datetime.now()
      current_time = now.strftime("%Y-%m-%d%H:%M")
      new_file_name = f"{current_time}{file.filename}"
      file.save(os.path.join('./static/images/menus', new_file_name))
      menu.file_name = new_file_name
    db.session.commit()
  return redirect(url_for('menu.show', menu_id=menu_id))

# 削除機能
@app.route('/setting/cafe/menu/delete/<int:menu_id>', methods=['GET', 'POST'])
def delete(menu_id):
  menu = Menu.query.get(menu_id)
  if menu:
    db.session.delete(menu)
    db.session.commit()
  return redirect('/setting/cafe/menu/list')