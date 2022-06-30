from flask import Blueprint, render_template
from postalcode import mod_dbconn

bp = Blueprint('main', __name__, url_prefix='/')    # blueprint 객체 생성

@bp.route('/')    # 라우팅 함수

def select():
    db_class = mod_dbconn.Database()

    sql = "SELECT postalcode FROM postalcode_db.postalcode LIMIT 10"
    row = db_class.executeAll(sql)

    print(row)

    return render_template('db.html', resultData=row[0])