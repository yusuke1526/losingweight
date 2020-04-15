from django.db import models
from django.conf import settings
from django.utils import timezone

class Measured(models.Model):
    weight = models.FloatField()
    body_fat_per = models.FloatField()
    measured_date = models.DateField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + '_' + str(self.measured_date)