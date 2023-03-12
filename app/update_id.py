from flask import render_template,request,redirect,url_for,flash
from app import app,db
from app.input_form import EntryForm 
from app.models import User,account_wise_amount,all_category_sub

@app.route("/update/<int:id>",methods =['POST','GET'])
def updateid(id):
    account_name,account_value = account_wise_amount() 
    cat_sub_name = all_category_sub()  
    #print (id)
    user = User.query.get_or_404(id)
    form = EntryForm()
    if request.method == 'POST':
        if form.is_submitted():
            user.account =(form.account.data).upper() 
            user.category =(form.category.data).upper() 
            user.subcategory =  (form.subcategory.data).upper()
            user.date = form.date.data  
            user.amount = form.amount.data 
            #print(form.subcategory.data) 
            db.session.commit()
            flash("Update ID {}".format(id), "success") 
            return(redirect(url_for('home')))
    elif request.method == 'GET':
        form.account.data = user.account
        form.category.data = user.category
        form.subcategory.data = user.subcategory
        form.date.data = user.date
        form.amount.data = user.amount   
    
    return render_template('add_id.html', 
                            form = form,
                            account=account_name,
                            category=cat_sub_name,
                            title="Update Entry")