from django.db import models
from django.contrib.auth.models import User
from teams.models import Team

STATUS = (0, 'Requested'), (1, 'Accepted'), (2, 'Declined'),
class Member(models.Model):

    owner = models.ForeignKey(
        User, related_name='member', on_delete=models.CASCADE
    )
    team = models.ForeignKey(
        Team, related_name='membership', on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)


    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'team']

    def __str__(self):
        return f'{self.owner} {self.team}'