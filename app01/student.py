from django.shortcuts  import render,redirect
import pymysql
from utils.sqlheper import SqlHeper
from django.http import HttpResponse

def student(request):
    #登录功能用装饰器实现一下

    obj = SqlHeper()
    sql = 'select student.id,student.name,student.class_id,classes.title from student left join classes on student.class_id=classes.id'
    student_list=obj.get_list(sql)
    class_list=obj.get_list('select id,title from classes')
    return render(request, "student.html", {'student_list': student_list,'class_list':class_list})

def add_student(request):
    obj = SqlHeper()
    if request.method == 'GET':
        class_list=obj.get_list("select id,title from classes")
        return render(request,'add_student.html',{'class_list':class_list})
    else:
        name = request.POST.get('name')
        title = request.POST.get('class_id')
        obj.modify("insert into student(name,class_id) value(%s,%s)",[name,title])
        return redirect('/student/')


def del_student(request):
    nid = request.GET.get('nid')
    obj.modify('delete from student where id=%s',nid)
    return redirect('/student/')

def edit_student(request):
    obj = SqlHeper()
    if request.method == 'GET':
        nid = request.GET.get('nid')
        sql = 'select id,title from classes'
        class_list = obj.get_list(sql)

        sql='select id,name,class_id from student where id=%s'
        result=obj.get_list(sql,[nid,],all=False)
        return render(request,"edit_student.html",{'class_list':class_list,'student_info':result})
    else:
        nid = request.GET.get('nid')
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')

        sql = 'update student set name=%s,class_Id=%s where id=%s'
        obj.modify(sql,[name,class_id,nid])
        return redirect('/student/')


def modal_add_student(request):
    obj = SqlHeper()
    ret = {'status':True,'msg':None}
    try:
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        obj.modify('insert into student(name,class_id) value(%s,%s)',[name,class_id])
    except Exception as e:
        ret['status'] = False
        ret['msg'] = str(e)
    import json
    return HttpResponse(json.dumps(ret))


def modal_edit_student(request):
    obj = SqlHeper()
    ret = {'status':True,'msg':None}
    try:
        name = request.POST.get('name')
        id = request.POST.get('id')
        class_id = request.POST.get('class_id')
        obj.modify('update student set name=%s,class_id=%s where id=%s',[name,class_id,id])
    except Exception as e:
        ret['status'] = False
        ret['msg'] = str(e)

    import json
    ret = json.dumps(ret)
    return HttpResponse(ret)




