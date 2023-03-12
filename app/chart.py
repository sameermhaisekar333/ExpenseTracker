from flask import render_template, json
from app import app
from app.models import (
    account_wise_amount,
    category_wise_amount,
    month_wise_amount,
    year_wise_amount,
)
import plotly
import plotly.express as px
import pandas as pd


@app.route("/chart", methods=["POST", "GET"])
def chart():

    account_name, account_amount = account_wise_amount()

    category_name, category_amount, sub_cat = category_wise_amount()

    year_month, year_month_amount = month_wise_amount()

    year_name, year_amount = year_wise_amount()

    month_data = list(zip(year_month, year_month_amount))
    df_month = pd.DataFrame(month_data, columns=["Month", "Amount"])
    # print(df_month.dtypes)
    df_month["Month"] = pd.to_datetime(df_month["Month"], format="%Y-%m")
    # print(type(df_month.iloc[0][0]))

    year_data = list(zip(year_name, year_amount))
    df_year = pd.DataFrame(year_data, columns=["Year", "Amount"])
    # print((df_year.dtypes))
    df_year["Year"] = pd.to_datetime(df_year["Year"], format="%Y")
    # print(type(df_year.iloc[0][0]))

    fig = px.pie(
        names=account_name,
        values=account_amount,
        template="plotly_dark",
        title="Account",
        labels={"names": "Account", "values": "Amount"},
    )
    fig.update_traces(textposition="inside", textinfo="percent+label")

    fig1 = px.pie(
        names=category_name,
        values=category_amount,
        template="plotly_dark",
        title="Category",
        labels={"names": "Category", "values": "Amount"},
    )
    fig1.update_traces(textposition="inside", textinfo="percent+label")

    fig2 = px.line(
        df_month, x="Month", y="Amount", title="Month", template="plotly_dark"
    )

    fig2.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list(
                [
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all"),
                ]
            ),
            activecolor="green",
            bgcolor="blue",
        ),
    )

    fig3 = px.line(df_year, x="Year", y="Amount", title="Year", template="plotly_dark")

    fig3.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list(
                [
                    dict(count=2, label="2y", step="year", stepmode="backward"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all"),
                ]
            ),
            activecolor="green",
            bgcolor="blue",
        ),
    )

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON1 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON3 = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template(
        "chart.html",
        graphJSON=graphJSON,
        graphJSON1=graphJSON1,
        graphJSON2=graphJSON2,
        graphJSON3=graphJSON3,
        title="Charts",
        active="Charts", 
    )
