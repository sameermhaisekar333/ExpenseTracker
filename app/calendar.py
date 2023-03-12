from flask import render_template, request
from app import app
from app.models import get_amount_for_dates 


@app.route("/calendar", methods=["POST", "GET"])
def calendar():
    amounts = get_amount_for_dates()
    return render_template(
        "calendar.html", title="Calendar", amounts=amounts, active="Calendar"
    )
