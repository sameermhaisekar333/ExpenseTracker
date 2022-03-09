from flask import render_template,json
from app import app
from app.models import User,get_category_for_account,get_amount_for_account 

@app.route("/accounts/<string:id>",methods =['POST','GET']) 
def accounts(id):
    posts = User.query.filter(User.account.in_([id])).order_by(User.date.desc()) 
    # for p in posts.items: 
    #     print(p)  
    category_name,category_amount = get_category_for_account(id) 
    year_name,year_amount         = get_amount_for_account(id)   
    return render_template('accounts.html',  
                            posts=posts,
                            title='Accounts',
                            heading = f'Account {id}',
                            category_name = json.dumps(category_name),
                            category_amount =json.dumps(category_amount),
                            year_name = json.dumps(year_name),
                            year_amount =json.dumps(year_amount))  