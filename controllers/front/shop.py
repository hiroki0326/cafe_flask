from flask import Blueprint, render_template

app = Blueprint('shop', __name__)

@app.route('/shop/')
def shop():
  return render_template('front/shop/home.html')