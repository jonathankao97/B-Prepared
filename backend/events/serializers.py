from rest_framework import serializers
from .models import Event, Task, Announcement


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('pk', 'name', 'date')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('pk', 'event', 'assigned_by',
                  'assigned_to', 'description', 'status', 'due_date')


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ('pk', 'event', 'sent_by', 'sent_to',
                  'description', 'sent_date')
