from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Task(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    assigned_by = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.CASCADE, related_name='assigned_by')
    description = models.TextField(max_length=255, blank=False, null=False)
    due_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Task({self.assigned_to}, {self.assigned_by})"

    def clean(self, *args, **kwargs):
        super(User, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(User, self).save(*args, **kwargs)


class UserTask(models.Model):
    task = models.ForeignKey(
        Task, blank=False, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"UserTask({self.task}, {self.user}, {self.status})"

    def clean(self, *args, **kwargs):
        super(User, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(User, self).save(*args, **kwargs)


class Announcement(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    sent_by = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.CASCADE, related_name='sent_by')
    sent_to = models.ManyToManyField(User, related_name='sent_to')
    description = models.TextField(max_length=255, blank=False, null=False)
    sent_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Announcement({self.title})"

    def clean(self, *args, **kwargs):
        super(User, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(User, self).save(*args, **kwargs)
