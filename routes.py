from flask import Blueprint, render_template, request, redirect, url_for

app = Blueprint('app', __name__)

from models import Post, Category
from app import db


@app.route('/')
def index():
    categories = Category.query.all()
    return render_template("index.html", categories=categories)


@app.route('/addcategory', methods=['POST'])
def add_category():
    name = request.form['category']
    category = Category(name)

    db.session.add(category)
    db.session.commit()

    return redirect(url_for('app.index'))


@app.route('/addpost', methods=['POST', 'GET'])
def add():
    content = request.form['content']
    category = db.session.query(Category).get(request.form['category'])
    post = Post(content, category)

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('app.index'))