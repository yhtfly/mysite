from django.shortcuts  import render,redirect,HttpResponse
import pymysql
from utils.sqlheper import SqlHeper

def teacher(request):
    #teacher_list = get_list('select id,name from teacher')
    obj = SqlHeper()
    sql = 'SELECT teacher.id as tid,teacher.name,classes.title from teacher ' \
          'left join teacher2class on teacher.id=teacher2class.teacher_id ' \
          'left join classes on classes.id = teacher2class.class_id'

    teacher_list=obj.get_list(sql)

    result = {}
    for row in teacher_list:
        tid = row['tid']
        if tid in result:
            result[tid]['titles'].append(row['title'])
        else:
            result[tid] = {'tid':row['tid'],'name':row['name'],'titles':[row['title'],]}
    return render(request,"teacher.html",{'teacher_list':result.values()})

def add_teacher(request):
    obj = SqlHeper()
    if request.method == 'GET':
        class_list = obj.get_list('select id,title from classes')
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
    obj = SqlHeper()
    nid = request.GET.get('nid')
    obj.modify('delete from teacher where id = %s',nid)
    return redirect(('/teacher/'))

def edit_teacher(request):
    if request.method == 'GET':
        nid = request.GET.get('tid')
        name = request.POST.get('name')

        obj = SqlHeper()
        teacher_info = obj.get_one('select id,name from teacher where id=%s',[nid,])
        class_list=obj.get_list('select id,title from classes')
        class_id_list = obj.get_list('select class_id from teacher2class where teacher_id=%s',[nid,])
        lst = []
        for item in class_id_list:
            lst.append(item['class_id'])
        class_id_list = lst
        return render(request,'edit_teacher.html',{'teacher_info':teacher_info,'class_list':class_list,'class_id_list':class_id_list,'tid':nid})
    else:
        nid = request.GET.get('nid')
        name = request.POST.get('name')
        class_id_list = request.POST.getlist('clsid')
        obj = SqlHeper()
        obj.modify('update teacher set name=%s where id=%s',[name,nid])

        print(nid)

        obj.modify('delete from teacher2class where teacher_id=%s',[nid,])

        lst = []
        for cls in class_id_list:
            lst.append((nid, cls))
        obj.multiple_modify('insert into teacher2class(teacher_id,class_id) value(%s,%s)', lst)
        obj.close()

        return redirect('/teacher/')


def get_all_class(request):
        obj = SqlHeper()
        class_list=obj.get_list('select id,title from classes')
        obj.close()
        import json
        return HttpResponse(json.dumps(class_list))


def modal_add_teacher(request):
    ret = {'status':True,'msg':None}
    try:
        teacher_name = request.POST.get('teacher_name')
        class_id_list = request.POST.getlist('class_id_list')

        print(teacher_name,class_id_list)
        obj = SqlHeper()
        teacher_id=obj.create('insert into teacher(name) value(%s)',[teacher_name])

        lst = []
        for cls in class_id_list:
            lst.append((teacher_id, cls))
        obj.multiple_modify('insert into teacher2class(teacher_id,class_id) value(%s,%s)', lst)
        obj.close()

    except Exception as e:
        ret['status']=False
        ret['msg']=str(e)

    import json
    return HttpResponse(json.dumps(ret))