from django.db import models
from django.db.models.fields import DateField

# Create your models here.
# thêm vào mysql python manage.py migrate
# python manage.py makemigrations
# python manage.py migrate
# python manage.py migrate --fake

class DoanhThu(models.Model):
    money = models.IntegerField()
    month = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)

class SoLuongKhach(models.Model):
    guests = models.IntegerField()
    inland = models.IntegerField()
    foreignG = models.IntegerField()
    month = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)

class Setting(models.Model):
    admin = models.CharField(max_length = 200)
    botname = models.CharField(max_length = 200)
    title = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True)

