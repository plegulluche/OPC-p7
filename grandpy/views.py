from grandpy import app
from grandpy.datacleaner import Datacleaner

from flask import render_template, request, make_response


@app.route("/", methods=["GET", "POST"])
def home():

    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():

    req = request.get_json()
    data_cleaner = Datacleaner(req)
    json_response = data_cleaner.response_if_all_status_ok()
    res = make_response(json_response, 200)
    return res
