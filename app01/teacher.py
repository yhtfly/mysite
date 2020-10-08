from django.shortcuts  import render,redirect
import pymysql
from utils.sqlheper import get_list,modify

def teacher(request):
    teacher_list = get_list('select id,name from teacher')
    return render(request,"teacher.html",{'teacher_list':teacher_list})

def add_teacher(request):
    if request.method == 'GET':
        return render(request,'add_teacher.html')
    else:
        name = request.POST.get('teacher_name')
        modify('insert into teacher(name) value(%s)',name)
        return redirect('/teacher/')

def del_teacher(request):
    nid = request.GET.get('id')
    modify('delete from teacher where id = %s',nid)
    return redirect(('/teacher/'))

def edit_teacher(request):
    if request.method == 'GET':
        nid = request.GET.get('id')
        result=get_list('select id,name from teacher where id=%s',[nid,],False)
        return render(request,"edit_teacher.html",{'result':result})
    else:
        name = request.POST.get('name')
        nid = request.GET.get('id')
        modify('update teacher set name=%s where id=%s',[name,nid])
        return redirect('/teacher/')
