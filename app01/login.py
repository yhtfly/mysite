from django.shortcuts  import render,redirect
import pymysql
from utils.sqlheper import SqlHeper
from django.http import HttpResponse


def login(request):
        if request.method =='GET':
            return render(request, 'login.html')
        else:
            username=request.POST.get('username')
            password = request.POST.get('password')
            if username=='zhangsan' and password=='123456':
                obj = redirect('/classes/')

                # import datetime
                # ct = datetime.datetime.utcnow()
                # v = datetime.timedelta(seconds=10)
                # value = ct + v
                # obj.set_cookie('ticket','lisi',expires=value)
                obj.set_signed_cookie('ticket','v1',salt='9999')
                #obj.set_cookie('ticket','zhangsan',max_age=10)
                return obj
            else:
                return render(request,'login.html')



