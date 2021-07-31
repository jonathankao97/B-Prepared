from ..models import Announcement, Task, UserTask
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from model_bakery import baker
from django.conf import settings
import datetime


User = get_user_model()
NUM_TESTS = 10


class AnnouncementModelManagerTest(TestCase):
    def test_object_manager_create_announcement(self):
        test_receivers = baker.make(User, _quantity=NUM_TESTS)
        test_announcement = Announcement.objects.create(
            sent_by=baker.make(User),
            title='test announcement',
            description='test description'
        )
        for receiver in test_receivers:
            test_announcement.sent_to.add(receiver)
        test_announcement.save()
        test_announcement_db = Announcement.objects.get(
            title='test announcement')

        self.assertEqual(test_announcement, test_announcement_db)


class TaskModeManagerTest(TestCase):
    def test_object_manager_create_task(self):
        test_task = Task.objects.create(
            assigned_by=baker.make(User),
            title='test task',
            description='test description',
            due_date=datetime.datetime.now()
        )
        test_task_db = Task.objects.get(
            title='test task'
        )

        self.assertEqual(test_task, test_task_db)

    def __str__(self):
        return f"Task({self.assigned_to}, {self.assigned_by})"

    def test_get_task_info(self):
        users = baker.make(User, _quantity=settings.NUM_TESTS)
        for user in users:
            self.assertEqual(user.get_full_name(),
                             f"{user.first_name} {user.last_name}")


class UserTaskModeManagerTest(TestCase):
    def test_object_manager_create_UserTasks(self):
        test_userTask = UserTask.objects.create(
            task=baker.make(Task),
            assigned_to=baker.make(User),
            status=False,
        )
        test_userTask_db = UserTask.objects.get(
            pk=test_userTask.pk
        )

        self.assertEqual(test_userTask, test_userTask_db)

    def test_object_manager_create_announcement_title_exceeds_character_limit(self):
        self.assertRaises(ValidationError, lambda: Announcement.objects.create(
            sent_by=baker.make(User),
            title='x' * 51,
            description='test description',
            sent_date=datetime.datetime.now()
        ))
