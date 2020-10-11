from django.shortcuts import render,redirect
import pymysql
from django.http import HttpResponse
from utils.sqlheper import SqlHeper


################################# index.py ###############################
def index(request):
    return render(request,'index.html')



def classes(request):
    obj = SqlHeper()
    class_list=obj.get_list("select id,title from classes")
    return render(request,'classes.html',{'class_list':class_list})


def add_class(request):
    obj = SqlHeper()
    if request.method == 'GET':
        return render(request, 'add_class.html')
    else:
        v = request.POST.get('title')
        if len(v) > 0:
            obj.modify("insert into classes(title) value(%s)",v)
            return redirect('/classes/')
        else:
            return render(request,'add_class.html',{'msg':'班级名称不能为空'})
def del_class(request):
    obj = SqlHeper()
    nid = request.GET.get('nid')
    obj.modify("delete from classes where id=%s", nid)
    return redirect('/classes/')

def edit_class(request):
    obj = SqlHeper()
    if request.method == 'GET':
        nid = request.GET.get('nid')
        result = obj.get_list("select id,title from classes where id=%s", [nid,],False)
        title=result['title']
        return render(request, "edit_class.html", {'nid': nid, 'title': title})
    else:
        nid = request.POST.get('nid')
        title = request.POST.get('title')
        obj.modify("update classes set title=%s where id=%s",[title,nid,])
        return redirect('/classes/')



############################ modal_add_class#########################

def modal_add_class(request):
    obj = SqlHeper()
    title = request.POST.get('title')
    if len(title):
        obj.modify('insert into classes(title) value(%s)',[title])
        return HttpResponse('OK')
    else:
        return HttpResponse('标题不能为空')


def modal_edit_class(request):
    obj = SqlHeper()
    ret={'status':True,'msg':None}

    try:
        nid = request.POST.get('nid')
        title = request.POST.get('title')
        obj.modify('update classes set title=%s where id=%s',[title,nid,])
    except Exception as e:
        ret['status'] = False
        ret['msg'] = str(e)
    finally:
        import json
        return HttpResponse(json.dumps(ret))


