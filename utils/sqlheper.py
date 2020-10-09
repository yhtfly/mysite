import pymysql

def get_list(sql,args=[],all=True):
    conn = pymysql.connect(host='59.110.239.77', port=3306, user='root', passwd='yhtfly', db='mydb')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql,args)

    if all:
        result = cursor.fetchall()
    else:
        result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def modify(sql,args):
    conn = pymysql.connect(host='59.110.239.77', port=3306, user='root', passwd='yhtfly', db='mydb')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    conn.commit()
    cursor.close()
    conn.close()

def create(sql,args):
    conn = pymysql.connect(host='59.110.239.77', port=3306, user='root', passwd='yhtfly', db='mydb')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    conn.commit()
    last_rowid= cursor.lastrowid
    cursor.close()
    conn.close()
    return last_rowid


class SqlHeper:
    def __init__(self):
        #可以把数据库连接写到数据库中
        self.connect()
    def connect(self):
        self.conn = pymysql.connect(host='59.110.239.77', port=3306, user='root', passwd='yhtfly', db='mydb')
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def get_list(self,sql,args):
        self.cursor.execute(sql, args)
        result = self.cursor.fetchall()
        return result

    def get_one(self,sql,args):
        self.cursor.execute(sql, args)
        result = self.cursor.fetone()
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



