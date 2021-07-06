from rest_framework import routers
from events.viewsets import EventView, TaskView, AnnouncementView

router = routers.DefaultRouter()
router.register('events', EventView, basename='event')
router.register('tasks', TaskView, basename='task')
router.register('announcements', AnnouncementView, basename='announcement')
