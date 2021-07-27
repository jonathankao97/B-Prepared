from rest_framework import routers
from users.viewsets import UserView
from events.viewsets import TaskView, UserTasksView, AnnouncementView


router = routers.DefaultRouter()
router.register('users', UserView, basename='user')
router.register('user-tasks', UserTasksView, basename='user-task')
router.register('tasks', TaskView, basename='task')
router.register('announcements', AnnouncementView, basename='announcement')
