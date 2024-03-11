from django.db import models

# Create your models here.

class RoomMember(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=200)
    insession = models.BooleanField(default=True)

class Account_Details(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=1000)
    password = models.CharField(max_length=200)
    

    def __str__(self):
        return self.name