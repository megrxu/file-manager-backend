from django.db import models

# Create your models here.

class Disk(models.Model):
    disk_device = models.CharField(max_length=100)
    disk_id = models.IntegerField(default=0)
    disk_mountpoint = models.CharField(max_length=100, default='')
    disk_size = models.IntegerField(default=0)
    disk_usedsize = models.IntegerField(default=0)
    disk_percent = models.FloatField(default=0)
    disk_shown = models.IntegerField(default=1)
    disk_mounted = models.IntegerField(default=0)

    def __str__(self):
        return self.disk_device