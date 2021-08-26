from django.db import models

# Create your models here.
class product(models.Model):
    pk_product = models.AutoField(primary_key=True, null=False, blank=False)
    code = models.CharField(max_length=9, null=False, blank=False)
    name = models.CharField(max_length= 50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.DecimalField(null=False, blank=False, max_digits=2, decimal_places=2)

class stock(models.Model):
    pk_stock = models.AutoField(primary_key=True, null=False, blank=False)
    amount = models.IntegerField(null=False, blank=False)
    fk_product = models.OneToOneField(product, null=False, blank=False, on_delete=models.CASCADE)

class tallas(models.Model):
    pk_tallas = models.AutoField(primary_key=True, null=False, blank=False)
    adultos = models.CharField(max_length=80, null=False, blank=False)
    niños = models.CharField(max_length=80, null=False, blank=False)

class marcas(models.Model):
    pk_marcas = models.AutoField(primary_key=True, null=False, blank=False)
    nike = models.CharField(max_length=80, null=False, blank=False)
    addidas = models.CharField(max_length=80, null=False, blank=False)
    puma = models.CharField(max_length=80, null=False, blank=False)
    converse = models.CharField(max_length=80, null=False, blank=False)



