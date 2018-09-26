from django.contrib import admin
from .models import Task, List


class ListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    #search_fields = ('title', 'name')
    #list_per_page = 25


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cr_date', 'due_date', 'owner', 'mark', 'list_id')
    list_display_links = ('id', 'name', 'cr_date', 'due_date', 'owner', 'mark', 'list_id')
    #search_fields = ('title', 'name', 'cr_date', 'due_date', 'owner', 'mark', 'list_id')
    #list_per_page = 25


admin.site.register(Task, TaskAdmin)
admin.site.register(List, ListAdmin)