from django.db import models


# Create your models here.

class RecentFiles(models.Model):
    filename = models.CharField(max_length=200)
    date = models.CharField(max_length=40)

    def __str__(self):
        return self.filename
