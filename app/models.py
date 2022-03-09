from app import db
from sqlalchemy import func 


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(20), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    subcategory = db.Column(db.String(20))
    date = db.Column(db.Date) 
    amount = db.Column(db.Float)

    def __repr__(self):
        return f" User( '{self.id}','{self.account}','{self.category}','{self.subcategory}','{self.date}','{self.amount}')"

 
def all_accounts():
    accounts = db.session.query(User.account,
                                db.func.sum(User.amount)
                                ).group_by(User.account
                                           ).order_by(User.account).all()
    #print(accounts)    
    return accounts

def all_category_sub():
    cat_sub_name = db.session.query(User.category,
                                    User.subcategory
                                    ).group_by(User.category,
                                               User.subcategory).all()  
    #print(cat_sub_name)
    return cat_sub_name    

def all_amounts_category_sub():
    by_catg_sub = db.session.query(User.category, 
                                   User.subcategory, 
                                    db.func.sum(User.amount)
                                    ).group_by(User.category
                                               ).order_by(User.category).all()
    #print(by_catg_sub)        
    return by_catg_sub    

def amount_by_month():
    by_month = db.session.query(func.strftime('%Y-%m', User.date), 
                                func.sum(User.amount)
                                ).group_by(func.strftime('%Y-%m', User.date)).all()
    #print(by_month)    
    return by_month

def amount_by_year():
    by_year = db.session.query(func.strftime('%Y', User.date),
                               func.sum(User.amount)
                               ).group_by(func.strftime('%Y', User.date)
                                          ).order_by(User.date).all()
    #print(by_year) 
    return by_year    

def account_wise_amount():
    accounts = all_accounts() 
    account_value = []
    accounts_name =[]
    
    for name,value, in accounts:
        #print(name,value)
        accounts_name.append(name)
        account_value.append(value)
    return accounts_name,account_value     

def category_wise_amount():
    category= all_amounts_category_sub()
    category_name =[]
    sub_name =[]
    category_amount =[]
    for c,s,v in category :
        category_name.append(c)
        sub_name.append(s)
        category_amount.append(v)
        #print(c,s,v) 
    return category_name,category_amount,sub_name  

def month_wise_amount():
    by_month = amount_by_month()
    year_month =[]
    year_month_amount =[]
    for  month,value in by_month :
        year_month.append(month)
        year_month_amount.append(value)
       # print(month,value)          
    return year_month,year_month_amount 

def year_wise_amount():
    by_year = amount_by_year()
    year_name =[]
    year_amount=[]

    for year,value in by_year:
        year_name.append(year)
        year_amount.append(value)
        #print (year,value)    
    return(year_name,year_amount)   

def get_account_for_date(day):
    #print(day)
    account_by = db.session.query(User.account,
                                  db.func.sum(User.amount)
                                  ).filter(User.date ==day
                                           ).group_by( User.account).all()
    #print(account_by)
    account_name=[]
    account_value= []
    for a,b in account_by:
        #print(a,b)
        account_name.append(a)
        account_value.append(b)
    return account_name,account_value

def get_category_for_date(day):
    category_by = db.session.query(User.category,
                                   db.func.sum(User.amount)
                                   ).filter(User.date ==day
                                            ).group_by( User.category).all()
    #print(category_by)
    category_name=[]
    category_value= []
    for a,b in category_by:
        #print(a,b)
        category_name.append(a)
        category_value.append(b)
    return category_name,category_value

def get_category_for_account(account):
    category_by = db.session.query(User.category,
                                   db.func.sum(User.amount)
                                   ).filter(User.account ==account
                                            ).group_by( User.category).all()
    #print(category_by)
    category_name=[]
    category_value= []
 
    for a,b in category_by:
        #print(a,b)
        category_name.append(a)
        category_value.append(b)
    return category_name,category_value

def get_amount_for_account(account):
    amount_by = db.session.query(func.strftime('%Y', User.date)
                                 ,db.func.sum(User.amount)
                                 ).filter(User.account ==account
                                          ).group_by( func.strftime('%Y', User.date)).all()
    #print(amount_by)
    year_name=[]
    year_value= []
    for a,b in amount_by:
        #print(a,b)
        year_name.append(a)
        year_value.append(b)
     
    return year_name,year_value

def get_account_for_category(category):
    account_by = db.session.query(User.account,
                                  db.func.sum(User.amount)
                                  ).filter(User.category ==category
                                           ).group_by( User.account).all()
    #print(account_by)
    account_name=[]
    account_value= []
   
    for a,b in account_by:
        #print(a,b)
        account_name.append(a)
        account_value.append(b)
    
    return account_name,account_value

def get_amount_for_category(category):
    amount_by = db.session.query(func.strftime('%Y', User.date),
                                 db.func.sum(User.amount)
                                 ).filter(User.category ==category
                                          ).group_by( func.strftime('%Y', User.date)).all()
    #print(amount_by)
    year_name=[]
    year_value= []
   
    for a,b in amount_by:
        #print(a,b)
        year_name.append(a)
        year_value.append(b)  
    return year_name,year_value 