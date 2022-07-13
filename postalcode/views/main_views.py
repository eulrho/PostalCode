import json

from flask import Blueprint, render_template, request, jsonify
from postalcode.mod_dbconn import Database

bp = Blueprint('main', __name__, url_prefix='/')  # blueprint 객체 생성


# Json data를 클라이언트->서버로 전달되지 않을 때 발생되는 오류 처리(Bad Request)
# 빈 curly brackets 를 반환하는 function
def on_json_loading_failed_return_dict(e):
    return {}


@bp.route('/', methods=['GET'])  # 라우팅 함수
def home():
    return render_template('home.html')


@bp.route('/ajax', methods=['GET'])
def select():
    # request.on_json_loading_failed 와 연결
    request.on_json_loading_failed = on_json_loading_failed_return_dict

    db_class = Database()
    data = request.args.get('input_pc')
    print(data)

    if data != '':
        # distinct : 중복 데이터 제거
        sql = "SELECT DISTINCT postalcode FROM postalcode_db.postalcode WHERE MATCH(postalcode) AGAINST(" + str(data) + " IN BOOLEAN MODE) LIMIT 7"
        row = db_class.executeAll(sql)
    return jsonify(row)

@bp.route('/testbody', methods=['GET'])
def testBody():
    data = request.get_data()
    print(data)
    return data