from app import app
from app.input_form import UploadFile
from app.models import insert_bulk
from flask import url_for, redirect, render_template, request, flash
from werkzeug.utils import secure_filename
import os, csv 


@app.route("/uploadfile", methods=["GET", "POST"])
def upload_file():
    file_list = uploaded_files_list()

    form = UploadFile()
    if request.method == "POST":
        if form.validate_on_submit():
            f = form.file.data
            filename = secure_filename(f.filename)
            # print(filename)
            form.file.data.save(app.config["UPLOAD_FOLDER"] + filename)
            flash("Uploaded {}".format(filename), "success")
            file_list = uploaded_files_list()

            return render_template(
                "upload.html",
                form=form,
                posts=file_list,
                title="Upload file",
                active="uploadFile",
            )

    return render_template(
        "upload.html",
        form=form,
        posts=file_list,
        title="Upload file",
        active="uploadFile",
    )


def uploaded_files_list():
    file_list = os.listdir(app.config["UPLOAD_FOLDER"])
    return file_list


@app.route("/bulk-insert/<string:id>", methods=["POST", "GET"])
def insert_file_content(id):
    # print(app.config['UPLOAD_FOLDER']+id)
    path = app.config["UPLOAD_FOLDER"] + id

    updated = insert_bulk(path=path)
    # print(updated)
    if updated:
        flash(" imported file  {} content to database".format(id), "success")
        return redirect(url_for("home"))
    flash("Error occured while importing {} to database".format(id), "danger")
    return redirect(url_for("upload_file"))


@app.route("/file-delete/<string:id>", methods=["POST", "GET"])
def delete_file_uploded(id):
    # print(app.config['UPLOAD_FOLDER']+id)
    path = app.config["UPLOAD_FOLDER"] + id
    os.remove(path)
    flash("Deleted  {}".format(id), "success")
    return redirect(url_for("upload_file"))


@app.route("/view-file-content/<string:id>", methods=["POST", "GET"])
def file_content(id):
    # print(app.config['UPLOAD_FOLDER']+id)

    path = app.config["UPLOAD_FOLDER"] + id
    with open(path, "r") as fp:
        data = csv.reader(fp) 
        # print(data)
        return render_template("file_content.html", data=data, name=id)
