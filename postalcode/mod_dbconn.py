import pymysql

class Database():
    def __init__(self):
        # database에 접근
        self.db = pymysql.connect(host='localhost',
                                  user='root',
                                  password='password',
                                  db='postalcode_db',
                                  charset='utf8')
        # database를 사용하기 위한 cursor 세팅
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row

    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    # 데이터 변화 적용
    def commit(self):
        self.db.commit()