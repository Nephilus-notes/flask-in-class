from app import db
from flask import render_template, request, redirect, url_for, flash
from app.blueprints.blog.models import Post, User
from flask_login import current_user, login_required
from . import bp as app



@app.route('/posts')
@login_required
def posts():
    all_posts = Post.query.all()
    return render_template('posts.html.j2', posts= all_posts)

# create a dynamic route to get a single post based on it's id
@app.route('/post/<id>')
@login_required
def post_by_id(id):
    post = Post.query.get(int(id))
    return render_template('post_single.html.j2', post=post)

@app.route('/create-post', methods=["POST"])
@login_required
def create_post():
    title = request.form['inputTitle']
    body = request.form['inputBody']
    new_post = Post(title=title, body=body, user_id=current_user.id)
    db.session.add(new_post)
    db.session.commit()
    flash("Post created successfully.", 'success')
    return redirect(url_for('blog.posts')) # similar redirect without import, using the function name
    return redirect('/blog/posts') # redirect imported from flask


