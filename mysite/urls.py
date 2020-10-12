"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views,teacher,student
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.index),
    path('classes/',views.classes),
    path('add_class/',views.add_class),
    path('del_class/',views.del_class),
    path('edit_class/',views.edit_class),
    path('get_all_class/',teacher.get_all_class),
    path('teacher/',teacher.teacher),
    path('add_teacher/',teacher.add_teacher),
    path('del_teacher/',teacher.del_teacher),
    path('edit_teacher/',teacher.edit_teacher),
    path('modal_add_teacher/',teacher.modal_add_teacher),
    path('student/',student.student),
    path('add_student/',student.add_student),
    path('modal_add_student/',student.modal_add_student),
    path('modal_edit_student/',student.modal_edit_student),

    path('del_student/',student.del_student),
    path('edit_student/',student.edit_student),
    path('modal_add_class/',views.modal_add_class),
    path('modal_edit_class/',views.modal_edit_class),
]
