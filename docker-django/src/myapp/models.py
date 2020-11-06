from django.db import models
from django.conf import settings
from django.utils import timezone



class proposal(models.Model):
    ethaddress = models.CharField(max_length=42)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=50)
    description = models.TextField()
    ethamount = models.FloatField()
    creation_date = models.DateTimeField(default=timezone.now())


class payouts(models.Model):
    relationship = 
    