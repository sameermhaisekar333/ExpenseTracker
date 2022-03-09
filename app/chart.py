
from flask import render_template,json
from app import app
from app.models import (account_wise_amount,
                        category_wise_amount,
                        month_wise_amount,
                        year_wise_amount) 

@app.route("/chart",methods =['POST','GET'])
def chart():

    
    account_name,account_amount = account_wise_amount() 

     
    category_name,category_amount,sub_cat = category_wise_amount() 
    
    
    year_month,year_month_amount = month_wise_amount() 

    
    year_name,year_amount = year_wise_amount()  
            
    return render_template("chart.html",
                        account_name=json.dumps(account_name),
                        account_amount= json.dumps(account_amount),
                        category_name = json.dumps(category_name),
                        category_amount = json.dumps(category_amount),
                        year_month = json.dumps(year_month),
                        year_month_amount = json.dumps(year_month_amount),
                        year_name = json.dumps(year_name),
                        year_amount = json.dumps(year_amount),
                        title ="Charts" 
                         )




  

