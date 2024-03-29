from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from boards.models import Board

STATUS = ((0, "To Do"), (1, "In Progress"), (2, "Complete"))
PRIORITY = ((0, "Low"), (1, "Medium"), (2, "High"))


class Task(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(
        Board, on_delete=models.CASCADE, related_name="tasks"
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    attachment = models.FileField(null=True, blank=True)
    duedate = models.DateField(null=True, blank=True)
    priority = models.IntegerField(choices=PRIORITY, default=0)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.owner}'s task"
