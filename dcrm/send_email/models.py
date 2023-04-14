from django.db import models

# Create your models here.
from django.db import models



class Notification(models.Model):
    recipient = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()