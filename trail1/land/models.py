from django.db import models
from datetime import datetime

# Create your models here.

class land(models.Model):
    area = models.IntegerField()
    land_image = models.URLField(max_length=200,default='')
    land_date = models.DateTimeField()
    land_info = models.TextField()
    owner_name = models.ForeignKey('users.User', on_delete=models.CASCADE)

