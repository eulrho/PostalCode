from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/')    # blueprint 객체 생성

@bp.route('/')    # 라우팅 함수
def home():
    return "HELLO"
