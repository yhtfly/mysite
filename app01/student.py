from django.shortcuts  import render,redirect
import pymysql
from utils.sqlheper import get_list,modify

def student(request):
    sql = 'select student.id,student.name,classes.title from student left join classes on student.class_id=classes.id'
    student_list=get_list(sql)
    return render(request, "student.html", {'student_list': student_list})

def add_student(request):
    if request.method == 'GET':
        conn = pymysql.connect(host='192.168.0.111', port=3306, user='root', passwd='htxq1230', db='mydb')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        effect_row = cursor.execute("select id,title from classes")
        class_list = cursor.fetchall()
        cursor.close()
        conn.close()
        return render(request,'add_student.html',{'class_list':class_list})
    else:
        name = request.POST.get('name')
        title = request.POST.get('class_id')
        conn = pymysql.connect(host='192.168.0.111', port=3306, user='root', passwd='htxq1230', db='mydb')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        effect_row = cursor.execute("insert into student(name,class_id) value(%s,%s)",[name,title])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/student')

def edit_student(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        sql = 'select id,title from classes'
        class_list = get_list(sql)

        sql='select id,name,class_id from student where id=%s'
        result=get_list(sql,[nid,],all=False)
        return render(request,"edit_student.html",{'class_list':class_list,'student_info':result})
    else:
        nid = request.GET.get('nid')
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')

        sql = 'update student set name=%s,class_Id=%s where id=%s'
        modify(sql,[name,class_id,nid])
        return redirect('/student/')

