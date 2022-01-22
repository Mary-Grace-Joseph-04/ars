from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    dob=models.DateField(null=True, blank=True)
    gender=models.CharField(max_length=32)
    nationality=models.CharField(max_length=32)
    address=models.CharField(max_length=1024)

    
class reservedetails(models.Model):
    # flight_no=models.CharField(max_length=20)
    # flight_name=models.CharField(max_length=20)
    # departure_time = models.TimeField()
    # arrival_time = models.TimeField()
    user = models.ForeignKey(MyUser, on_delete=models.PROTECT)
    departure_city = models.CharField(max_length=20)
    arrival_city= models.CharField(max_length=20)
    Class=models.CharField(max_length=20)
    date = models.DateField()

    
    class Meta:
        db_table ="reservedetails"

class places(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class classes(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name