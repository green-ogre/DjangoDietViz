from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class GraphData(models.Model):
    date_started = models.DateField(default=timezone.now)
    calorie_goal = models.IntegerField()
    protein_goal = models.IntegerField()
    data = models.JSONField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.email