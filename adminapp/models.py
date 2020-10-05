from django.db import models

class AdminLoginModel(models.Model):
    name=models.CharField(max_length=200)
    password=models.CharField(max_length=100)
class RoomModel(models.Model):
    id=models.AutoField(primary_key=True)
    type=models.CharField(max_length=200)
    capacity=models.IntegerField()
    add_date=models.DateField()
    image=models.ImageField(upload_to='room_images/')
    status=models.CharField(max_length=100,default="available")

