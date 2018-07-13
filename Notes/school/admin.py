from django.contrib import admin

# Register your models here.
from school.models import Student, Graden


class AddInfo(admin.StackedInline):
    model = Student
    extra = 5


class StudentAdmin(admin.ModelAdmin):
    list_display = ['s_name', 's_gender', 's_age', 's_graden']
    search_fields = ['s_name']
    list_per_page = 2
    list_filter = ['s_graden']


class GradenAdmin(admin.ModelAdmin):
    list_display = ['g_name', 'g_num']
    search_fields = ['g_name']
    list_per_page = 2
    list_filter = ['g_num']
    inlines = [AddInfo]


admin.site.register(Student, StudentAdmin)
admin.site.register(Graden, GradenAdmin)


