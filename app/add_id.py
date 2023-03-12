from flask import render_template, url_for, redirect, request, flash
from app import app, db
from app.models import User, account_wise_amount, all_category_sub
from app.input_form import EntryForm 


@app.route("/add", methods=["POST", "GET"])
def add():
    account_name, account_value = account_wise_amount()

    cat_sub_name = all_category_sub()

    form = EntryForm()
    if form.is_submitted():
        result = request.form
        # print(result.get('amount'))
        user = User(
            amount=form.amount.data,
            account=(form.account.data).upper(),
            category=(form.category.data).upper(),
            subcategory=(form.subcategory.data).upper(),
            date=form.date.data,
        )
        db.session.add(user)
        db.session.commit()
        flash("Added new Transaction", "success")
        return redirect(url_for("home"))
    return render_template(
        "add_id.html",
        form=form,
        account=account_name,
        category=cat_sub_name,
        title="Add New Entry",
        active="Add New Entry",
    )
