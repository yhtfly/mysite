from django.shortcuts  import render,redirect,HttpResponse
from django.views import View
from app01.models import UserGroup,UserInfo

from django.core.paginator import Paginator,Page,PageNotAnInteger,EmptyPage

def paging(request):

    #django自带的分页
    current_page = request.GET.get('page')
    user_list=UserInfo.objects.all()
    paginator = Paginator(user_list,10)

    try:
        posts = paginator.page(current_page)
    except PageNotAnInteger as e:
        posts = paginator.page(1)
    except EmptyPage as e:
        posts = paginator.page(1)
    return render(request,'paging.html',{'posts':posts})

#     per_page:每页显示条目数量
#     count:数据总个数
#     num_pages:总页数
#     page_range:总页数的索引范围，如：(1,10),(1,200)
#     page:page对象



#     has_next :是否有下一页
#     next_page_number 下一页页码
#     has_previous: 是否有上一页
#     previous_page_number:上一页页码
#     object_list:分页之后的数据列表
#     numbler:当前页
#     paginator:paginator对象


