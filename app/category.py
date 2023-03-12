from flask import render_template, json
from app import app
from app.models import User, get_amount_for_category, get_account_for_category
import plotly
import plotly.express as px

@app.route("/category/<string:id>", methods=["POST", "GET"])
def category(id):
    posts = User.query.filter(User.category.in_([id])).order_by(User.date.desc())
    # for p in posts.items:
    #     print(p)
    account_name, account_amount = get_account_for_category(id)
    year_name, year_amount = get_amount_for_category(id)

    fig = px.pie(
        names=account_name,
        values=account_amount,
        hole=0.3,
        template="plotly_dark",
        title="Accounts",
        labels={"names": "Account", "values": "Amount"},
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
        "category.html",
        posts=posts,
        title="Category",
        heading=f"Category {id}",
        graphJSON=graphJSON,
        graphJSON1=graphJSON1,
    )
