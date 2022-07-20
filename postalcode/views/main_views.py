from flask import Blueprint, render_template, request, jsonify
from postalcode.mod_dbconn import Database

bp = Blueprint('main', __name__, url_prefix='/')  # blueprint 객체 생성


# Json data를 클라이언트->서버로 전달되지 않을 때 발생되는 오류 처리(Bad Request)
# 빈 curly brackets 를 반환하는 function
def on_json_loading_failed_return_dict(e):
    return {}


@bp.route('/')  # 라우팅 함수
def home():
    return render_template('home.html')


@bp.route('/search', methods=['GET'])
def select():
    # request.on_json_loading_failed 와 연결
    request.on_json_loading_failed = on_json_loading_failed_return_dict

    db_class = Database()
    data = request.args.get('srchAddress')

    if data != '':
        # distinct : 중복 데이터 제거
        # 불린 모드 시 특정 한 컬럼에 있는 data만 인식(ex. 경상남도 창원시는 sido와 sigungu data를 합한 것이므로 검색x)하므로 자연어 모드 사용
        # 검색어에 ""를 씌워 한 덩어리로 묶음
        sql = 'SELECT DISTINCT * FROM postalcode_db.postalcode WHERE MATCH(searchColumn) AGAINST("' + str(data) + '") LIMIT 7'
        row = db_class.executeAll(sql)
    return jsonify(row)

@bp.route('/result', methods=['GET','POST'])
def result():
    if request.method == 'POST':
        result = request.form
        print(result)
        return render_template('address.html', res=result)

# test
@bp.route('/testbody', methods=['GET'])
def testBody():
    data = request.get_data()
    print(data)
    return data