from django.db import models

# Create your models here.
class Comidas(models.Model):
    pk_comidas = models.AutoField(primary_key=True)
    menus = models.CharField(max_length=50, blank=False, null=False)
    precio = models.CharField(max_length=50, blank=False, null=False)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=True)
