from flask import render_template, json
from app import app
from app.models import User, get_category_for_account, get_amount_for_account

import plotly
import plotly.express as px


@app.route("/accounts/<string:id>", methods=["POST", "GET"])
def accounts(id):
    posts = User.query.filter(User.account.in_([id])).order_by(User.date.desc())
    # for p in posts.items:
    #     print(p)
    category_name, category_amount = get_category_for_account(id)
    year_name, year_amount = get_amount_for_account(id)
    fig = px.pie(
        names=category_name,
        values=category_amount,
        hole=0.3,
        template="plotly_dark",
        title="Category",
        labels={"names": "Category", "values": "Amount"},
    )
    fig.update_traces(textposition="inside", textinfo="percent+label")

    fig1 = px.line(
        x=year_name,
        y=year_amount,
        markers=True,
        template="plotly_dark",
        title="Year",
        labels={"x": "Year", "y": "Amount"},
    )

    # Create graphJSON
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON1 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template(
        "accounts.html",
        posts=posts,
        title="Accounts",
        heading=f"Account {id}",
        graphJSON=graphJSON,
        graphJSON1=graphJSON1,
    )
