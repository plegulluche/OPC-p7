from grandpy import app
from grandpy.datacleaner import Datacleaner

from flask import render_template, request, redirect, url_for, jsonify, make_response

@app.route('/', methods=['GET', 'POST'])
def home():

    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    
    req = request.get_json()
    print('pierre debug req: ', req, type(req))
    data_cleaner = Datacleaner(req['text'])
    json_response = data_cleaner.response_if_all_status_ok()
    print('pierre debug json resp : ', json_response, type(json_response))
    res = make_response(json_response, 200)
    print('pierre debug res: ', res , type(res))
    return res