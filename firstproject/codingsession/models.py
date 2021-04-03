from django.db import models
from django.utils import timezone
from django.utils.timezone import utc

# Create your models here.

class CodingSession(models.Model):
    name = models.CharField(max_length=1024, unique=True)
    language = models.CharField(max_length=1024)
    link = models.CharField(max_length=2048)
    starting_time = models.DateTimeField(default=timezone.now ,blank=True)

    def __str__(self):
        return self.name