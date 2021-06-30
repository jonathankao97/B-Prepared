from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('events', views.EventView)
router.register('tasks', views.TaskView)
router.register('announcements', views.AnnouncementView)


urlpatterns = [
    path('', include(router.urls)),
]
