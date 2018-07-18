from django.conf.urls import url

from myApp import views

urlpatterns = [
    url(r'^index/', views.index,name='index'),
    url(r'^login/',views.login,name='login'),
    url(r'^home/',views.home,name='home'),
    url(r'^quite/',views.quite,name='logout'),
    url(r'^upload/',views.upload,name='upload'),
]
