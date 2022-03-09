from flask import render_template,request,redirect,url_for
from app import app,db
from app.models import User

@app.route("/delete/<int:id>",methods =['POST','GET'])
def delete(id):
    #print (id)
    user = User.query.get_or_404(id)
    #print(user)  
    db.session.delete(user) 
    db.session.commit()   
    return redirect(url_for('home')) 