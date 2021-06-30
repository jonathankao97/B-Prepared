from django.contrib import admin
from .models import Event, Task, Announcement


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    search_fields = ('name', 'date')
    list_per_page = 25


class TaskAdmin(admin.ModelAdmin):
    list_display = ('description', 'assigned_by',
                    'assigned_to', 'get_event', 'status')
    list_per_page = 25


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('description', 'date', 'sent_by',
                    'get_sent_list', 'get_event')
    list_per_page = 25


admin.site.register(Event, EventAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
