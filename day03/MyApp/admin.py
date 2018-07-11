from django.contrib import admin

# Register your models here.
from MyApp.models import Hero, Hero_Book


class Hero_BookInline(admin.StackedInline):
    model = Hero_Book
    extra = 3


class HeroAdmin(admin.ModelAdmin):
    # hero=Hero()
    list_display = ['h_name','h_age','h_gender','h_birthday']
    search_fields = ['h_name']
    list_filter = ['h_age']
    list_per_page = 2
    fieldsets = [
        ('第一组',{'fields':['h_name','h_age']}),
        ('第二组',{'fields':['h_gender','h_birthday']}),
    ]
    inlines = [Hero_BookInline]


class Hero_BookAdmin(admin.ModelAdmin):

    list_display = ['b_name','b_info','b_number','b_date']
    search_fields = ['b_name']
    list_filter = ['b_date']
    list_per_page = 2
    fieldsets = [
        ('第一组',{'fields':['b_name','b_info']}),
        ('第二组',{'fields':['b_number','b_date']}),
    ]


admin.site.register(Hero,HeroAdmin)
admin.site.register(Hero_Book,Hero_BookAdmin)
