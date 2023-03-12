from flask import render_template,json
from app import app
from app.models import User,get_account_for_date,get_category_for_date 

import plotly
import plotly.express as px
import pandas as pd 

@app.route("/dates/<string:id>",methods =['POST','GET']) 
def dates(id):
    posts = User.query.filter(User.date.in_([id]))
    
    d = []
    for p in posts:
        a = {
            "id": p.id,
            "account": p.account,
            "category": p.category,
            "subcategory": p.subcategory,
            "date": p.date,
            "amount": p.amount,
        }
        d.append(a)
    # print(d)
    df = pd.DataFrame(d)
    # print(df)
      
    account_name,account_amount = get_account_for_date(id) 
    category_name,category_amount = get_category_for_date(id)
    
    fig = px.sunburst(
        df,
        path=["date", "account", "category", "subcategory"],
        values="amount",
        template="plotly_dark",
        title="Date ",
    )
    
    fig1 = px.pie(
        names=account_name,
        values=account_amount,
        hole=0.3,
        template="plotly_dark",
        title="Accounts",
        labels={"names": "Account", "values": "Amount"},
    )
    
    fig1.update_traces(textposition="inside", textinfo="percent+label")

    fig2 = px.bar(
        x=category_name,
        y=category_amount,
        labels={"x": "Category", "y": "Amount", "color": "Category"},
        color=category_name,
        template="plotly_dark",
        title="Category",
    )

    # Create graphJSON
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON1 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template( 
        "dates.html",
        posts=posts,
        title="Date",
        heading=f"Date {id}",
        graphJSON=graphJSON,
        graphJSON1=graphJSON1,
        graphJSON2=graphJSON2,
    )
