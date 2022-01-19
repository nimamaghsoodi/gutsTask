from django.db import models

# Create your models here.

class EP_ENGINE_USAGE(models.Model):
    POD_NAME = models.CharField(max_length=225)
    CPU_USAGE = models.IntegerField()
    RAM_USAGE = models.IntegerField()
    TIME_STAMP = models.CharField(max_length=225)

    def __str__(self):
        return self.POD_NAME