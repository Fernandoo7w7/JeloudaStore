from django.db import models

# Create your models here.
class product(models.Model):
    pk_product = models.AutoField(primary_key=True, null=False, blank=False)
    code = models.CharField(max_length=9, null=False, blank=False)
    name = models.CharField(max_length= 50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    image1 = models.URLField(max_length=800, default='https://i.imgur.com/llmXU3a.jpg', blank=False, null=False)
    image2 = models.URLField(max_length=800, default='https://i.imgur.co m/KDHLAjk.jpg', blank=False, null=False)


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
    nike = models.IntegerField(null=False, blank=False)
    addidas = models.IntegerField(null=False, blank=False)
    puma = models.IntegerField(null=False, blank=False)
    converse = models.IntegerField(null=False, blank=False)



