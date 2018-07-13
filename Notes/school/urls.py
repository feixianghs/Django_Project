from django.conf.urls import url

from school import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_stu/$',views.add_stu),
]
