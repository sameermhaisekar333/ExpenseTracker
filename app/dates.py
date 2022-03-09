from flask import render_template,json
from app import app
from app.models import User,get_account_for_date,get_category_for_date 

@app.route("/dates/<string:id>",methods =['POST','GET']) 
def dates(id):
    posts = User.query.filter(User.date.in_([id]))
    # for p in posts.items:
    #     print(p)    
    account_name,account_amount = get_account_for_date(id) 
    category_name,category_amount = get_category_for_date(id)
    return render_template('dates.html',  
                            posts=posts,
                            title='Date',
                            heading = f'Date {id}',
                            account_name = json.dumps(account_name),
                            account_amount =json.dumps(account_amount),
                            category_name = json.dumps(category_name),
                            category_amount =json.dumps(category_amount),
                            )  