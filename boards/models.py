from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Board(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name}"
