from rest_framework import serializers, viewsets
from .models import Task, UserTask, Announcement
from .serializers import TaskSerializer, UserTasksSerializer, AnnouncementSerializer


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserTasksView(viewsets.ModelViewSet):
    queryset = UserTask.objects.all()
    serializer_class = UserTasksSerializer


class AnnouncementView(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
