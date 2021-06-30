from django.shortcuts import render
from rest_framework import viewsets, serializers
from .models import Event, Task, Announcement
from .serializers import EventSerializer, TaskSerializer, AnnouncementSerializer


class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    fields = '__all__'


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    fields = '__all__'


class AnnouncementView(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    fields = '__all__'
