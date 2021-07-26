from rest_framework import serializers
from .models import Task, UserTask, Announcement


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('pk', 'assigned_by', 'title', 'description', 'due_date')


class UserTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTask
        fields = ('pk', 'task', 'user', 'status')


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ('pk', 'sent_by', 'sent_to', 'title',
                  'description', 'sent_date')
