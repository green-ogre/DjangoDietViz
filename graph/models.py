from django.db import models
from django.contrib.auth.models import User

class GraphData(models.Model):
    # Storing all the data as a concatenated string :)
    weight = models.CharField(max_length=365, default='')
    calories = models.CharField(max_length=365, default='')
    protein = models.CharField(max_length=365, default='')