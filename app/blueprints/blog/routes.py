from app import db
from flask import render_template, request, redirect, url_for
from app.blueprints.blog.models import Post, User
from . import bp as app

@app.route('/blog/posts')
def posts():
    all_posts = Post.query.all()
    return render_template('posts.html.j2', posts= all_posts)

# create a dynamic route to get a single post based on it's id
@app.route('/blog/post/<id>')
def post_by_id(id):
    post = Post.query.get(int(id))
    return render_template('post_single.html.j2', post=post)

@app.route('/blog/create-post', methods=["POST"])
def create_post():
    title = request.form['inputTitle']
    body = request.form['inputBody']
    new_post = Post(title=title, body=body, user_id=2)
    db.session.add(new_post)
    db.session.commit()
    return redirect(url_for('blog.posts')) # similar redirect without import, using the function name
    return redirect('/blog/posts') # redirect imported from flask


