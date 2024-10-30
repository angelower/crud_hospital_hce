from django.db import models

# Create your models here.
class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    documento = models.TextField(max_length=30)
    nombre = models.TextField(max_length=100)
    edad = models.IntegerField()
    eps = models.TextField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes/' , null=True)

class Test(models.Model):
    id = models.AutoField(primary_key=True)
    documento = models.TextField(max_length=50)
    testname = models.TextField(max_length=100)
    testretult = models.IntegerField()

