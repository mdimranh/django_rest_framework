from django.contrib import admin
from .models import Student
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'name', 'department', 'email']
    search_fields = ['name', 'email', 'student_id']
    list_filter = ['term', 'level', 'department']
admin.site.register(Student, StudentAdmin)