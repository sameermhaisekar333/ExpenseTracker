from flask import render_template, Response, send_file
from app import app
from app.models import write_to_csv
  

@app.route("/getcsv", methods=["GET"])  # this is a job for GET, not POST
def download_csv():

    write_to_csv()

    return send_file(
        "../data.csv",
        mimetype="text/csv",
        download_name="model-data.csv",
        as_attachment=True,
    )
