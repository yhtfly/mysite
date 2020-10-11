import pymysql

class SqlHeper:
    def __init__(self):
        #可以把数据库连接写到数据库中
        self.connect()
    def connect(self):
        self.conn = pymysql.connect(host='59.110.239.77', port=3306, user='root', passwd='yhtfly', db='mydb')
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def get_list(self,sql,args=[]):
        self.cursor.execute(sql, args)
        result = self.cursor.fetchall()
        return result

    def get_one(self,sql,args):
        self.cursor.execute(sql, args)
        result = self.cursor.fetchone()
        return result

    def modify(self,sql,args):
        self.cursor.execute(sql,args)
        self.conn.commit()

    def create(self,sql,args):
        self.cursor.execute(sql, args)
        self.conn.commit()
        return self.cursor.lastrowid

    def multiple_modify(self,sql,args):
        self.cursor.executemany(sql,args)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()



