from django.shortcuts  import render,redirect
import pymysql
from utils.sqlheper import get_list,modify,create,SqlHeper

def teacher(request):
    #teacher_list = get_list('select id,name from teacher')
    sql = 'SELECT teacher.id as tid,teacher.name,classes.title from teacher ' \
          'left join teacher2class on teacher.id=teacher2class.teacher_id ' \
          'left join classes on classes.id = teacher2class.class_id'

    teacher_list=get_list(sql)

    result = {}
    for row in teacher_list:
        tid = row['tid']
        if tid in result:
            result[tid]['titles'].append(row['title'])
        else:
            result[tid] = {'tid':row['tid'],'name':row['name'],'titles':[row['title'],]}
    return render(request,"teacher.html",{'teacher_list':result.values()})

def add_teacher(request):
    if request.method == 'GET':
        class_list = get_list('select id,title from classes')
        return render(request,'add_teacher.html',{'class_list':class_list})
    else:
        obj = SqlHeper()
        name = request.POST.get('name')
        teacher_id=obj.create('insert into teacher(name) value(%s)',name)
        class_list = request.POST.getlist('class_ids')

        lst = []
        for cls in class_list:
            lst.append((teacher_id,cls))
        obj.multiple_modify('insert into teacher2class(teacher_id,class_id) value(%s,%s)',lst)
        obj.close()
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
