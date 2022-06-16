from django.db import models

# Create your models here.

class FamiliarConviviente(models.Model):
    
    nombre = models.CharField(max_length=30)
    nacimiento = models.DateField()
    edad = models.IntegerField()
    parentezco = models.CharField(max_length=30)
    
class FamiliarExtendida(models.Model):
    
    nombre = models.CharField(max_length=30)
    nacimiento = models.DateField()
    edad = models.IntegerField()
    parentezco = models.CharField(max_length=30)
