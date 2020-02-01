from django.db import models

# Create your models here.

class Dicty(models.Model):
    name      = models.CharField(max_length=50)

class KeyVal(models.Model):
    container = models.ForeignKey(Dicty, db_index=True,on_delete=models.CASCADE)
    key       = models.CharField(max_length=240, db_index=True)
    value     = models.CharField(max_length=240, db_index=True)

class Beacon(models.Model):
    name=models.CharField(max_length=40,unique=False)
    uuid=models.CharField(max_length=20,unique=True)
    major=models.IntegerField()
    minor=models.IntegerField()
    data=KeyVal()
