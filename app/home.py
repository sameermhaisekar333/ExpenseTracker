from flask import render_template, request
from app import app
from app.models import User 


@app.route("/", methods=["POST", "GET"]) 
def home():
    page = request.args.get("page", 1, type=int)

    posts = User.query.order_by(User.date.desc()).paginate(page=page, per_page=10)
    return render_template("home.html", posts=posts, title="Home", active="Home")
