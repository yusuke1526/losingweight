from django.db import models
from django.conf import settings

class Diet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    name = models.CharField(max_length=100)
    calorie = models.IntegerField()

    def __str__(self):
        return self.name