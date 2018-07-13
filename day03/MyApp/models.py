from django.db import models


# Create your models here.


class Hero_Book(models.Model):
    b_name = models.CharField(max_length=40, verbose_name='书名')
    b_info = models.CharField(max_length=4000, verbose_name='简介')
    b_date = models.DateTimeField(verbose_name='出版时间')
    b_number = models.IntegerField(verbose_name='出版量')
    b_hero = models.ForeignKey('Hero')

    def __str__(self):
        return self.b_name

    class Meta:
        verbose_name = '发行书籍'
        verbose_name_plural = "发行书籍"


class Hero(models.Model):
    h_name = models.CharField(max_length=40, verbose_name='姓名')
    h_age = models.IntegerField(default=30, verbose_name='年龄')
    # sex = ((1, '男'), (2, '女'),)
    h_gender = models.IntegerField(choices=((1, '男'), (2, '女'),), verbose_name='性别')
    h_birthday = models.DateTimeField(verbose_name='出生日期')

    

    def __str__(self):
        return self.h_name

    class Meta:
        verbose_name = '英雄'
        verbose_name_plural = "英雄"

    # def gender(self):
    #     if self.h_gender:
    #         return '男'
    #     else:
    #         return '女'
    #
    # gender.short_description = '性别'
