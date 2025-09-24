from django.db import models
from django.utils.timezone import now

class Visit(models.Model):
    ip = models.GenericIPAddressField()
    user_agent = models.TextField()
    path = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=now)