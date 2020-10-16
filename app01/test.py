from django.shortcuts  import render,redirect,HttpResponse
import pymysql
from django.views import View
from utils.sqlheper import SqlHeper
def test(request):
    from app01.models import UserGroup,UserInfo
    #插入
    #UserGroup.objects.create(title='小英')
    #UserInfo.objects.create(user='张三',password='pwd',ug_id=1)

    #查询
    #group_list=UserGroup.objects.all()
    #user_list=UserInfo.objects.all()
    #group_lsit=UserGroup.objects.filter(id=1)
    #group_lsit=UserGroup.objects.filter(id__gt=1)
    #group_lsit=UserGroup.objects.filter(id__lt=2)

    #删除
    #UserGroup.objects.filter(id=2).delete()

    #更新
    #UserGroup.objects.filter(id=1).update(title='鸣人')

    result=UserInfo.objects.all()
    for row in result:
        print(row.user,row.password,row.ug_id,row.ug.title)
    return HttpResponse('hello 视图')


class login(View):
    def get(self,request):
        return HttpResponse('view.get')
    def post(self,request):
        return HttpResponse('view.post')

