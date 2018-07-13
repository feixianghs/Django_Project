from django.db import models


# Create your models here.
class Graden(models.Model):
    g_name = models.CharField(max_length=40, default='python1805',verbose_name='班级')
    g_num = models.IntegerField(default=20, verbose_name='人数')

    def __str__(self):
        return self.g_name

    class Meta:
        verbose_name = '班级表'
        verbose_name_plural = '班级表'


class Student(models.Model):
    s_name = models.CharField(max_length=40, verbose_name='姓名')
    s_gender = models.IntegerField(choices=((1, '男'), (2, '女')), verbose_name='性别')
    s_age = models.IntegerField(default=20, verbose_name='年龄')
    s_graden = models.ForeignKey(Graden, verbose_name='班级')

    def __str__(self):
        return self.s_name

    class Meta:
        verbose_name = '学生表'
        verbose_name_plural = '学生表'
