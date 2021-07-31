from ..models import Announcement, Task, UserTask
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from model_bakery import baker
from django.contrib.auth import get_user_model
import datetime

User = get_user_model()
NUM_TESTS = 10


class TestAnnouncementCreateEndpoint(APITestCase):
    def setUp(self):
        self.create_url = reverse('announcement-list')

    def test_create_announcement(self):
        """
        Ensure we can create a new announcement
        """

        test_user = baker.make(User)
        test_receivers = baker.make(User, _quantity=NUM_TESTS)
        test_receivers_array = []
        for receiver in test_receivers:
            test_receivers_array.append(receiver.pk)

        data = {
            'title': 'test title',
            'sent_by': test_user.pk,
            'sent_to': test_receivers_array,
            'description': 'test description'
        }

        response = self.client.post(self.create_url, data, format='json')

        announcement = Announcement.objects.get(title=data['title'])
        sent_to_list = announcement.sent_to.all()
        sent_to_pk_list = []
        for user in sent_to_list:
            sent_to_pk_list.append(user.pk)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(announcement.title, data['title'])
        self.assertEqual(announcement.sent_by.pk, data['sent_by'])
        self.assertEqual(sent_to_pk_list, data['sent_to'])
        self.assertEqual(announcement.description, data['description'])

    def test_create_announcement_with_missing_title(self):
        """
        Ensure error codes when missing title
        """

        test_user = baker.make(User)
        test_receivers = baker.make(User, _quantity=NUM_TESTS)
        test_receivers_array = []
        for receiver in test_receivers:
            test_receivers_array.append(receiver.pk)

        data = {
            'sent_by': test_user.pk,
            'sent_to': test_receivers_array,
            'description': 'test description'
        }

        response = self.client.post(self.create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(Announcement.DoesNotExist,
                          lambda: Announcement.objects.get(description=data['description']))

    def test_create_announcement_with_missing_sent_by(self):
        """
        Ensure error codes when missing sent_by
        """

        test_receivers = baker.make(User, _quantity=NUM_TESTS)
        test_receivers_array = []
        for receiver in test_receivers:
            test_receivers_array.append(receiver.pk)

        data = {
            'title': 'test title',
            'sent_to': test_receivers_array,
            'description': 'test description'
        }

        response = self.client.post(self.create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(Announcement.DoesNotExist,
                          lambda: Announcement.objects.get(description=data['description']))

    def test_create_announcement_with_missing_sent_to(self):
        """
        Ensure error codes when missing sent_to
        """

        test_user = baker.make(User)

        data = {
            'title': 'test title',
            'sent_by': test_user.pk,
            'description': 'test description'
        }

        response = self.client.post(self.create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(Announcement.DoesNotExist,
                          lambda: Announcement.objects.get(description=data['description']))

    def test_create_announcement_with_missing_description(self):
        """
        Ensure error codes when missing description
        """

        test_user = baker.make(User)
        test_receivers = baker.make(User, _quantity=NUM_TESTS)
        test_receivers_array = []
        for receiver in test_receivers:
            test_receivers_array.append(receiver.pk)

        data = {
            'title': 'test title',
            'sent_by': test_user.pk,
            'sent_to': test_receivers_array
        }

        response = self.client.post(self.create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(Announcement.DoesNotExist,
                          lambda: Announcement.objects.get(title=data['title']))

    def test_create_announcement_with_invalid_title(self):
        """
        Ensure error codes when invalid title
        """
        test_user = baker.make(User)
        test_receivers = baker.make(User, _quantity=NUM_TESTS)
        test_receivers_array = []
        for receiver in test_receivers:
            test_receivers_array.append(receiver.pk)

        data = {
            'title': '',
            'sent_by': test_user.pk,
            'sent_to': test_receivers_array,
            'description': 'test description'
        }

        response = self.client.post(self.create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(Announcement.DoesNotExist,
                          lambda: Announcement.objects.get(description=data['description']))

    def test_create_announcement_with_invalid_sent_by(self):
        """
        Ensure error codes when invalid sent_by
        """
        test_receivers = baker.make(User, _quantity=NUM_TESTS)
        test_receivers_array = []
        for receiver in test_receivers:
            test_receivers_array.append(receiver.pk)

        data = {
            'title': 'test title',
            'sent_by': '',
            'sent_to': test_receivers_array,
            'description': 'test description'
        }

        response = self.client.post(self.create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(Announcement.DoesNotExist,
                          lambda: Announcement.objects.get(title=data['title']))

    def test_create_announcement_with_invalid_sent_to(self):
        """
        Ensure error codes when invalid sent_to
        """
        test_user = baker.make(User)

        data = {
            'title': 'test title',
            'sent_by': test_user.pk,
            'sent_to': '',
            'description': 'test description'
        }

        response = self.client.post(self.create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(Announcement.DoesNotExist,
                          lambda: Announcement.objects.get(title=data['title']))

    def test_create_announcement_with_invalid_description(self):
        """
        Ensure error codes when invalid description
        """
        test_user = baker.make(User)
        test_receivers = baker.make(User, _quantity=NUM_TESTS)
        test_receivers_array = []
        for receiver in test_receivers:
            test_receivers_array.append(receiver.pk)

        data = {
            'title': 'test title',
            'sent_by': test_user.pk,
            'sent_to': test_receivers_array,
            'description': ''
        }

        response = self.client.post(self.create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(Announcement.DoesNotExist,
                          lambda: Announcement.objects.get(title=data['title']))


class TestAnnouncementRetrieveEndpoint(APITestCase):
    def setUp(self):
        self.announcement = baker.make(Announcement)
        self.retrieve_url = reverse(
            'announcement-detail', kwargs={'pk': self.announcement.pk})

    def test_retrieve_announcement(self):
        """
        Ensure we can retrieve a announcement and response only contains expected fields
        """
        response = self.client.get(self.retrieve_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            set(response.data.keys()),
            {'pk', 'title', 'sent_by', 'sent_to', 'description', 'sent_date'})

    def test_retrieve_announcement_not_found(self):
        """
        Ensure error is thrown if announcement is not found
        """
        url = reverse('announcement-detail',
                      kwargs={'pk': self.announcement.pk + 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TestAnnouncementUpdateEndpoint(APITestCase):
    def setUp(self):
        self.announcement = baker.make(Announcement)
        self.update_url = reverse(
            'announcement-detail', kwargs={'pk': self.announcement.pk})

    def test_partial_update_user(self):
        """
        Ensure we can partial update a announcement
        """
        data = {
            'title': 'updated title',
            'description': 'updated description',
        }

        response = self.client.patch(self.update_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_full_update_user(self):
        """
        Ensure we can full update a annnouncement
        """

        new_user = baker.make(User)
        new_receivers = baker.make(User, _quantity=NUM_TESTS)
        new_receivers_array = []
        for receiver in new_receivers:
            new_receivers_array.append(receiver.pk)
        data = {
            'title': 'new title',
            'sent_by': new_user.pk,
            'sent_to': new_receivers_array,
            'description': 'new description'
        }

        response = self.client.put(self.update_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestAnnouncementDeleteEndpoint(APITestCase):
    def setUp(self):
        self.announcement = baker.make(Announcement)
        self.delete_url = reverse(
            'announcement-detail', kwargs={'pk': self.announcement.pk})

    def test_delete_announcement(self):
        """
        Ensure we can delete a announcement
        """
        announcement = baker.make(Announcement)

        response = self.client.delete(self.delete_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_user_not_found(self):
        pass


class TestAnnouncementListEndpoint(APITestCase):
    def setUp(self):
        self.announcement1 = baker.make(Announcement)
        self.announcement2 = baker.make(Announcement)
        self.list_url = reverse('announcement-list')

    def test_list_announcements(self):
        """
        Ensure we can list all users
        """
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


# ------------ TASK TESTS ------------

# ------------ TASK TESTS ------------

# ------------ TASK TESTS ------------

# ------------ TASK TESTS ------------

# ------------ TASK TESTS ------------

# ------------ TASK TESTS ------------


class TestTaskCreateEndpoint(APITestCase):
    def setUp(self):
        self.create_url = reverse('task-list')

    def test_create_task(self):
        """
        Ensure we can create a new task
        """

        test_user = baker.make(User)

        data = {
            'title': 'test title',
            'assigned_by': test_user.pk,
            'description': 'test description'
        }

        response = self.client.post(self.create_url, data, format='json')

        task = Task.objects.get(title=data['title'])

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(task.title, data['title'])
        self.assertEqual(task.assigned_by.pk, data['assigned_by'])
        self.assertEqual(task.description, data['description'])

    def test_create_task_with_missing_title(self):
        """
        Ensure error codes when missing title
        """

        test_user = baker.make(User)

        data = {
            'assigned_by': test_user.pk,
            'description': 'test description'
        }

        response = self.client.post(self.create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(Task.DoesNotExist,
                          lambda: Task.objects.get(description=data['description']))

    def test_create_task_with_missing_assigned_by(self):
        """
        Ensure error codes when missing assigned_by
        """

        data = {
            'title': 'test title',
            'description': 'test description'
        }

        response = self.client.post(self.create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(Task.DoesNotExist,
                          lambda: Task.objects.get(description=data['description']))

    def test_create_task_with_missing_description(self):
        """
        Ensure error codes when missing description
        """

        test_user = baker.make(User)

        data = {
            'title': 'test title',
            'assigned_by': test_user.pk
        }

        response = self.client.post(self.create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(Task.DoesNotExist,
                          lambda: Task.objects.get(title=data['title']))

    def test_create_task_with_invalid_title(self):
        """
        Ensure error codes when invalid title
        """
        test_user = baker.make(User)

        data = {
            'title': '',
            'assigned_by': test_user.pk,
            'description': 'test description'
        }

        response = self.client.post(self.create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(Task.DoesNotExist,
                          lambda: Task.objects.get(description=data['description']))

    def test_create_task_with_invalid_assigned_by(self):
        """
        Ensure error codes when invalid assigned_by
        """

        data = {
            'title': 'test title',
            'assigned_by': '',
            'description': 'test description'
        }

        response = self.client.post(self.create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(Task.DoesNotExist,
                          lambda: Task.objects.get(title=data['title']))

    def test_create_task_with_invalid_description(self):
        """
        Ensure error codes when invalid description
        """
        test_user = baker.make(User)

        data = {
            'title': 'test title',
            'assigned_by': test_user.pk,
            'description': ''
        }

        response = self.client.post(self.create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(Task.DoesNotExist,
                          lambda: Task.objects.get(title=data['title']))


class TestTaskRetrieveEndpoint(APITestCase):
    def setUp(self):
        self.task = baker.make(Task)
        self.retrieve_url = reverse(
            'task-detail', kwargs={'pk': self.task.pk})

    def test_retrieve_task(self):
        """
        Ensure we can retrieve a task and response only contains expected fields
        """
        response = self.client.get(self.retrieve_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            set(response.data.keys()),
            {'pk', 'title', 'assigned_by', 'description', 'due_date'})

    def test_retrieve_task_not_found(self):
        """
        Ensure error is thrown if task is not found
        """
        url = reverse('task-detail',
                      kwargs={'pk': self.task.pk + 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TestTaskUpdateEndpoint(APITestCase):
    def setUp(self):
        self.task = baker.make(Task)
        self.update_url = reverse(
            'task-detail', kwargs={'pk': self.task.pk})

    def test_partial_update_user(self):
        """
        Ensure we can partial update a task
        """
        data = {
            'title': 'updated title',
            'description': 'updated description',
        }

        response = self.client.patch(self.update_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_full_update_user(self):
        """
        Ensure we can full update a annnouncement
        """

        new_user = baker.make(User)

        data = {
            'title': 'new title',
            'assigned_by': new_user.pk,
            'description': 'new description'
        }

        response = self.client.put(self.update_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestTaskDeleteEndpoint(APITestCase):
    def setUp(self):
        self.task = baker.make(Task)
        self.delete_url = reverse(
            'task-detail', kwargs={'pk': self.task.pk})

    def test_delete_task(self):
        """
        Ensure we can delete a task
        """
        task = baker.make(Task)

        response = self.client.delete(self.delete_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_user_not_found(self):
        pass


class TestTaskListEndpoint(APITestCase):
    def setUp(self):
        self.task1 = baker.make(Task)
        self.task2 = baker.make(Task)
        self.list_url = reverse('task-list')

    def test_list_tasks(self):
        """
        Ensure we can list all tasks
        """
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        # ------------ USERTASK TESTS ------------

        # ------------ USERTASK TESTS ------------

        # ------------ USERTASK TESTS ------------

        # ------------ USERTASK TESTS ------------

        # ------------ USERTASK TESTS ------------

        # ------------ USERTASK TESTS ------------


class TestUserTaskCreateEndpoint(APITestCase):
    def setUp(self):
        self.create_url = reverse('user-task-list')

    def test_create_user_task(self):
        """
        Ensure we can create a new user user_task
        """

        test_user = baker.make(User)
        test_task = baker.make(Task)

        data = {
            'task': test_task.pk,
            'user': test_user.pk,
            'status': False
        }

        response = self.client.post(self.create_url, data, format='json')

        user_task = UserTask.objects.get(task=data['task'])

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(user_task.task.pk, data['task'])
        self.assertEqual(user_task.user.pk, data['user'])
        self.assertEqual(user_task.status, data['status'])

    def test_create_user_task_with_missing_task(self):
        """
        Ensure error codes when missing task
        """

        test_user = baker.make(User)

        data = {
            'user': test_user.pk,
            'status': False
        }

        response = self.client.post(self.create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(UserTask.DoesNotExist,
                          lambda: UserTask.objects.get(user=data['user']))

    def test_create_UserTask_with_missing_user(self):
        """
        Ensure error codes when missing user
        """

        test_task = baker.make(Task)

        data = {
            'task': test_task.pk,
            'status': False
        }

        response = self.client.post(self.create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(UserTask.DoesNotExist,
                          lambda: UserTask.objects.get(task=data['task']))

    def test_create_UserTask_with_missing_status(self):
        """
        Ensure no error codes when missing status
        """

        test_user = baker.make(User)
        test_task = baker.make(Task)

        data = {
            'user': test_user.pk,
            'task': test_task.pk
        }

        response = self.client.post(self.create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_UserTask_with_invalid_task(self):
        """
        Ensure error codes when invalid task
        """
        test_user = baker.make(User)

        data = {
            'task': '',
            'user': test_user.pk,
            'status': False
        }

        response = self.client.post(self.create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(UserTask.DoesNotExist,
                          lambda: UserTask.objects.get(user=data['user']))

    def test_create_UserTask_with_invalid_user(self):
        """
        Ensure error codes when invalid assigned_by
        """

        test_task = baker.make(Task)

        data = {
            'task': test_task.pk,
            'user': '',
            'status': False
        }

        response = self.client.post(self.create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(UserTask.DoesNotExist,
                          lambda: UserTask.objects.get(task=data['task']))

    def test_create_UserTask_with_invalid_status(self):
        """
        Ensure error codes when invalid description
        """

        test_task = baker.make(Task)
        test_user = baker.make(User)

        data = {
            'task': test_task.pk,
            'user': test_user.pk,
            'status': ''
        }

        response = self.client.post(self.create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(UserTask.DoesNotExist,
                          lambda: UserTask.objects.get(task=data['task']))


class TestUserTaskRetrieveEndpoint(APITestCase):
    def setUp(self):
        self.user_task = baker.make(UserTask)
        self.retrieve_url = reverse(
            'user-task-detail', kwargs={'pk': self.user_task.pk})

    def test_retrieve_task(self):
        """
        Ensure we can retrieve a user_task and response only contains expected fields
        """
        response = self.client.get(self.retrieve_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            set(response.data.keys()),
            {'pk', 'task', 'user', 'status'})

    def test_retrieve_user_task_not_found(self):
        """
        Ensure error is thrown if user_task is not found
        """
        url = reverse('user-task-detail',
                      kwargs={'pk': self.user_task.pk + 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TestUserTaskUpdateEndpoint(APITestCase):
    def setUp(self):
        self.user_task = baker.make(UserTask)
        self.update_url = reverse(
            'user-task-detail', kwargs={'pk': self.user_task.pk})

    def test_partial_update_user_task(self):
        """
        Ensure we can partial update a user_task
        """

        data = {
            'status': True
        }

        response = self.client.patch(self.update_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_full_update_user_task(self):
        """
        Ensure we can full update a user task
        """

        new_user = baker.make(User)
        new_task = baker.make(Task)

        data = {
            'task': new_task.pk,
            'user': new_user.pk,
            'status': True
        }

        response = self.client.put(self.update_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestUserTaskDeleteEndpoint(APITestCase):
    def setUp(self):
        self.user_task = baker.make(UserTask)
        self.delete_url = reverse(
            'user-task-detail', kwargs={'pk': self.user_task.pk})

    def test_delete_user_task(self):
        """
        Ensure we can delete a user_task
        """
        user_task = baker.make(UserTask)

        response = self.client.delete(self.delete_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_user_not_found(self):
        pass


class TestUserTaskListEndpoint(APITestCase):
    def setUp(self):
        self.user_task1 = baker.make(UserTask)
        self.user_task2 = baker.make(UserTask)
        self.list_url = reverse('user-task-list')

    def test_list_user_tasks(self):
        """
        Ensure we can list all user_tasks
        """
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
