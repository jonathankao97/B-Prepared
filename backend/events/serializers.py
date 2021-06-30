from rest_framework import serializers
from .models import Event, Task, Announcement


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'date')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'event', 'assigned_by',
                  'assigned_to', 'description', 'status')


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ('id', 'event', 'sent_by', 'sent_to',
                  'description', 'date')
