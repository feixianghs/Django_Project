from django.contrib import admin

# Register your models here.
from APP.models import Student, Grade


def gender(self):
    if self.s_sex:
        return '女'
    else:
        return '男'


gender.short_description = '性别'


class StudentInline(admin.TabularInline):
    model = Student
    extra = 3


class GradeAdmin(admin.ModelAdmin):
    inlines = [StudentInline]
   # list_display = ['s_name', 'g_number']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['s_name', 's_age', 's_bir', gender]
    search_fields = ['s_name']
    list_filter = ['s_name', 's_age', 's_bir', 's_sex']


admin.site.register(Student, StudentAdmin)
admin.site.register(Grade, GradeAdmin)
