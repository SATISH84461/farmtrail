from django.db import models
from datetime import datetime

# Create your models here.

class categories(models.Model):
    cat_name = models.CharField(max_length=64,unique=True)

class crops(models.Model):
    crop_name = models.CharField(max_length = 64)
    crop_image = models.URLField(max_length=200,default='')
    crop_quantity = models.IntegerField()
    crop_info = models.TextField()
    crop_date = models.DateTimeField()
    cat_id = models.ForeignKey('categories', on_delete=models.CASCADE)
    owner_name = models.ForeignKey('users.User', on_delete=models.CASCADE)
