from django.db import models

# Create your models here.

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_date = models.DateField()
    description = models.TextField()