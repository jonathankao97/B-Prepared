from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import DateTimeField
from django.utils import timezone

User = get_user_model()


class Event(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    date = models.DateTimeField(blank=True, null=True)


class Task(models.Model):
    event = models.ForeignKey(
        Event, blank=True, null=True, on_delete=models.CASCADE)
    assigned_by = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.CASCADE, related_name='assigned_by')
    assigned_to = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.CASCADE, related_name='assigned_to')

    description = models.CharField(max_length=50, blank=False, null=False)
    status = models.BooleanField(default=False)

    def get_event(self):
        if self.event:
            return self.event.name
        else:
            return ""


class Announcement(models.Model):
    event = models.ForeignKey(
        Event, blank=True, null=True, on_delete=models.CASCADE)
    sent_by = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.CASCADE, related_name='sent_by')
    sent_to = models.ManyToManyField(User, related_name='sent_to')

    description = models.TextField(max_length=255, blank=False, null=False)
    date = models.DateTimeField(default=timezone.now)

    def get_sent_list(self):
        return " ".join([p.username for p in self.sent_to.all()])

    def get_event(self):
        if self.event:
            return self.event.name
        else:
            return ""
