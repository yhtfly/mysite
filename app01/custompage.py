from django.shortcuts  import render,redirect,HttpResponse
from app01.models import UserGroup,UserInfo
from utils import pager



def custom(request):
    all_count = UserInfo.objects.all().count()

    current_page = request.GET.get('page')
    page_info = pager.PageInfo(current_page,all_count,10,'/custompage.html')
    user_list=UserInfo.objects.all()[page_info.start():page_info.end()]
    # print(user_list)
    # return HttpResponse('123')
    return render(request,'custompage.html',{'user_list':user_list,'page_info':page_info})