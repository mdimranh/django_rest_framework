from django.contrib import admin

from .models import Contact

class ConatctAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'msg', 'created_at']
	search_fields = ['name', 'email', 'message']
	list_filter = ['created_at']

admin.site.register(Contact, ConatctAdmin)
