from random import *

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from school.models import Student, Graden


def index(request):
    return render(request, 'web/html/index.html')


def add_stu(request):
    stu=Student()
    stu.s_name=choice(['小王','小李','小张','小红','小赵','小明','小华','小孙','小平','小小'])
    stu.s_age=randint(20,30)
    graden=Graden.objects.last()
    stu.s_graden=graden
    stu.s_gender=choice([1,2])
    stu.save()
    context={'stu.s_name':stu.s_name,'stu.s_age':stu.s_age,'stu.s_gender':stu.s_gender,'stu.s_graden':stu.s_graden}
    return render(request,'web/html/add_stu.html',context)
    # return HttpResponse("添加成功")