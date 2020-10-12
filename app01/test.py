from django.shortcuts  import render,redirect,HttpResponse
import pymysql
from utils.sqlheper import SqlHeper
def test(request):
    return render(request,'test.html')