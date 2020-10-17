from django.shortcuts  import render,redirect,HttpResponse
from django.views import View
from app01.models import UserGroup,UserInfo
def test(request):

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

    # obj = UserGroup.objects.all().first()
    # for row in obj.userinfo_set.all():
    #     print(row.user,row.age)


    obj = UserGroup.objects.all()
    for row in obj:
        print(row.id,row.title,row.userinfo_set.filter(name='李四')[0].name)

    return HttpResponse('hello 视图')


