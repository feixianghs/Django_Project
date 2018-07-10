from django.db import models


# Create your models here.

class Grade(models.Model):
    g_name = models.CharField(verbose_name='班级名称', default='python1805', max_length=40)
    g_number = models.PositiveIntegerField(default=40,verbose_name='班级人数')

    class Meta:
        verbose_name = '班级'
        verbose_name_plural = "班级"

    def __str__(self):
        return self.g_name


class Student(models.Model):
    s_name = models.CharField(max_length=40, verbose_name='姓名')
    s_age = models.IntegerField(default=18,verbose_name='年龄')
    s_sex = models.BooleanField(default=True,verbose_name='性别')
    s_bir = models.DateTimeField(auto_now_add=True,verbose_name='生日')
    s_grade = models.ForeignKey(Grade, null=True)


    class Meta:
        verbose_name = '学生'
        verbose_name_plural = "学生"


    def __str__(self):
        return self.s_name
