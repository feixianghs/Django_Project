from django.conf.urls import url

from MyApp import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^add_hero/$', views.add_hero),
]