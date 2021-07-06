from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Event(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Event({self.name}, {self.date})"


class Task(models.Model):
    event = models.ForeignKey(
        Event, blank=True, null=True, on_delete=models.CASCADE)
    assigned_by = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.CASCADE, related_name='assigned_by')
    assigned_to = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.CASCADE, related_name='assigned_to')

    description = models.CharField(max_length=50, blank=False, null=False)
    status = models.BooleanField(default=False)
    due_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Task({self.assigned_to}, {self.assigned_by})"


class Announcement(models.Model):
    event = models.ForeignKey(
        Event, blank=True, null=True, on_delete=models.CASCADE)
    sent_by = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.CASCADE, related_name='sent_by')
    sent_to = models.ManyToManyField(User, related_name='sent_to')

    description = models.TextField(max_length=255, blank=False, null=False)
    sent_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Announcement({self.sent_by}, {self.date})"
