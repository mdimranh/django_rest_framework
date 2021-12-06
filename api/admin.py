from django.contrib import admin

from .models import Student

class StudentAdmin(admin.ModelAdmin):
	list_display = ['name', 'id', 'roll', 'city']
	search_fields = ['id', 'name']
	list_filter = ['city']

admin.site.register(Student, StudentAdmin)
