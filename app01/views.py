from django.shortcuts import render,redirect
import pymysql
from django.http import HttpResponse
from utils.sqlheper import get_list,modify


################################# index.py ###############################
def index(request):
    return render(request,'index.html')



def classes(request):

    conn = pymysql.connect(host='192.168.0.111',port=3306,user='root',passwd='htxq1230',db='mydb')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    effect_row = cursor.execute("select id,title from classes")
    class_list = cursor.fetchall()
    cursor.close()
    conn.close()


    return render(request,'classes.html',{'class_list':class_list})


def add_class(request):
    if request.method == 'GET':
        return render(request, 'add_class.html')
    else:
        v = request.POST.get('title')
        if len(v) > 0:
            conn = pymysql.connect(host='192.168.0.111', port=3306, user='root', passwd='htxq1230', db='mydb')
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            effect_row = cursor.execute("insert into classes(title) value(%s)",v)
            conn.commit()
            cursor.close()
            conn.close()
            return redirect('/classes/')
        else:
            return render(request,'add_class.html',{'msg':'班级名称不能为空'})
def del_class(request):
    nid = request.GET.get('nid')
    conn = pymysql.connect(host='192.168.0.111', port=3306, user='root', passwd='htxq1230', db='mydb')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    effect_row = cursor.execute("delete from classes where id=%s", nid)
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/classes/')

def edit_class(request):

    if request.method == 'GET':
        nid = request.GET.get('nid')
        conn = pymysql.connect(host='192.168.0.111', port=3306, user='root', passwd='htxq1230', db='mydb')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        effect_row = cursor.execute("select id,title from classes where id=%s", nid)
        result = cursor.fetchone()
        title=result['title']

        conn.commit()
        cursor.close()
        conn.close()
        return render(request, "edit_class.html", {'nid': nid, 'title': title})
    else:
        nid = request.POST.get('nid')
        title = request.POST.get('title')

        print(nid,title)
        conn = pymysql.connect(host='192.168.0.111', port=3306, user='root', passwd='htxq1230', db='mydb')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        effect_row = cursor.execute("update classes set title=%s where id=%s",[title,nid,])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/classes/')



############################ modal_add_class#########################

def modal_add_class(request):
    title = request.POST.get('title')
    if len(title):
        modify('insert into classes(title) value(%s)',[title])
        return HttpResponse('OK')
    else:
        return HttpResponse('标题不能为空')



