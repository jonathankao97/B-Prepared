from django.contrib import admin
from .models import Event, Task, Announcement


class EventAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'date')
    search_fields = ('pk', 'name', 'date')
    list_per_page = 25


class TaskAdmin(admin.ModelAdmin):
    list_display = ('pk', 'description', 'event', 'assigned_by',
                    'assigned_to', 'status', 'due_date')
    list_per_page = 25


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('pk', 'description', 'event', 'sent_by', 'sent_date')
    list_per_page = 25


admin.site.register(Event, EventAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
