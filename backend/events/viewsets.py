from rest_framework import viewsets
from .models import Event, Task, Announcement
from .serializers import EventSerializer, TaskSerializer, AnnouncementSerializer


class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class AnnouncementView(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
