from flask import Blueprint, render_template, request, jsonify, make_response
from postalcode.mod_dbconn import Database

bp = Blueprint('main', __name__, url_prefix='/')    # blueprint 객체 생성

# 빈 curly brackets 를 반환하는 function
def on_json_loading_failed_return_dict(e):
	return {}

@bp.route('/', methods=['GET'])    # 라우팅 함수
# def home():
#     return render_template('home.html')
#
#     db_class = Database()
#     data = request.get_json()
#     # data = {"input_pc":'256'}
#     keyword = data['input_pc']
#     # data = '"256"'
#     # distinct : 중복 데이터 제거
#     sql = "SELECT DISTINCT postalcode FROM postalcode_db.postalcode WHERE MATCH(postalcode) AGAINST(" + keyword + " IN BOOLEAN MODE) LIMIT 10"
#     # sql = "SELECT DISTINCT postalcode FROM postalcode_db.postalcode WHERE MATCH(postalcode) AGAINST('"256"') IN BOOLEAN MODE) LIMIT 10"
#     row = db_class.executeAll(sql)
#     # return render_template('db.html', resultData=row)
#     # result = jsonify(row)
#     res = make_response(keyword)
#     return res
#     # return jsonify(row)
# def home():
#     return render_template('home.html')

@bp.route('/ajax', methods=['GET'])
def select():
    # request.on_json_loading_failed 와 연결
    request.on_json_loading_failed = on_json_loading_failed_return_dict

    db_class = Database()
    data = request.get_json()
    print(data)
    # data = {"input_pc":'256'}
    inputData = data['input_pc']
    print(inputData)
    # data = '"256"'
    # distinct : 중복 데이터 제거
    sql = "SELECT DISTINCT postalcode FROM postalcode_db.postalcode WHERE MATCH(postalcode) AGAINST(" + inputData + " IN BOOLEAN MODE) LIMIT 10"
    # sql = "SELECT DISTINCT postalcode FROM postalcode_db.postalcode WHERE MATCH(postalcode) AGAINST('"256"') IN BOOLEAN MODE) LIMIT 10"
    row = db_class.executeAll(sql)
    return make_response(jsonify(row))
    # return jsonify(row)
