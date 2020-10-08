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



