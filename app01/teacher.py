from django.shortcuts  import render,redirect
import pymysql

def teacher(request):
    conn = pymysql.connect(host='192.168.0.111',port=3306,user='root',passwd='htxq1230',db='mydb')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    effect_row = cursor.execute('select id,name from teacher')
    teacher_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return render(request,"teacher.html",{'teacher_list':teacher_list})

def add_teacher(request):
    if request.method == 'GET':
        return render(request,'add_teacher.html')
    else:
        name = request.POST.get('teacher_name')
        conn = pymysql.connect(host="192.168.0.111",port=3306,user='root',passwd='htxq1230',db='mydb')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        effect_row = cursor.execute('insert into teacher(name) value(%s)',name)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/teacher/')

def del_teacher(request):
    nid = request.GET.get('id')
    conn = pymysql.connect(host='192.168.0.111',port=3306,user='root',passwd='htxq1230',db='mydb')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    effect_row=cursor.execute('delete from teacher where id = %s',nid)
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(('/teacher/'))

def edit_teacher(request):
    if request.method == 'GET':
        nid = request.GET.get('id')
        conn = pymysql.connect(host='192.168.0.111',port=3306,user='root',passwd='htxq1230',db='mydb')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        effect_row=cursor.execute('select id,name from teacher where id=%s',nid)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return render(request,"edit_teacher.html",{'result':result})
    else:
        name = request.POST.get('name')
        print(name)
        nid = request.GET.get('id')
        print(nid)
        conn = pymysql.connect(host='192.168.0.111', port=3306, user='root', passwd='htxq1230', db='mydb')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        effect_row = cursor.execute('update teacher set name=%s where id=%s',[name,nid])
        print(effect_row)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/teacher/')
