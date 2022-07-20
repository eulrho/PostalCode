from postalcode import create_app

app = create_app('/path/to/config/cfg')
app.run(debug=True, threaded=True)     # 디버그 모드. 어플리케이션을 실행할 때 파라미터로 넘겨줌
# app.run(host="0.0.0.0")     # 외부에서 접근가능케 한다.