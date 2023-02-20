from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Team(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to="images/", default="../default_team_mi0sbj.png")
    members = models.ManyToManyField(User, related_name="teams")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name}"
