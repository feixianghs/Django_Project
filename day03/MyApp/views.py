from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from MyApp.models import Hero


def add_hero(request):
    hero=Hero()
    hero.h_name='陈独秀'
    hero.h_age='40'
    hero.h_gender='True'
    hero.save()
    context={'hero.h_name':hero.h_name,'hero.h_age':hero.h_age,'hero.h_gender':hero.h_gender}
    return render(request,'add_html',context)


def index(request):
    return render(request,'index.html')