from flask import render_template,json
from app import app
from app.models import User,get_amount_for_category,get_account_for_category

@app.route("/category/<string:id>",methods =['POST','GET']) 
def category(id):
    posts = User.query.filter(User.category.in_([id])).order_by(User.date.desc())
    # for p in posts.items: 
    #     print(p)    
    account_name,acount_amount =get_account_for_category(id)
    year_name,year_amount = get_amount_for_category(id)
    return render_template('category.html', 
                        posts=posts,
                        title='Category',
                        heading = f'Category {id}',
                        account_name =json.dumps(account_name),
                        acount_amount = json.dumps(acount_amount),
                        year_name = json.dumps(year_name),
                        year_amount= json.dumps(year_amount))   