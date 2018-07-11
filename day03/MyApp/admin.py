from django.contrib import admin

# Register your models here.
from MyApp.models import Hero, Hero_Book

admin.site.register(Hero)
admin.site.register(Hero_Book)


