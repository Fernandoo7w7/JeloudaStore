from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class resourceProduct (resources.ModelResource):
    class Meta:
        model = product

class adminProduct(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['code','name', 'description', 'price']
    resource_class = resourceProduct

admin.site.register(product, adminProduct)


class resourceStock (resources.ModelResource):
    class Meta:
        model = stock

class adminStock(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['pk_stock']
    list_display = ['fk_product','amount']
    resource_class = resourceStock

admin.site.register(stock, adminStock)

class resourceTallas (resources.ModelResource):
    class Meta:
        model = tallas

class adminTallas(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['pk_tallas']
    list_display = ['adultos','niños']
    resource_class = resourceTallas

admin.site.register(tallas, adminTallas)

class resourceMarcas (resources.ModelResource):
    class Meta:
        model = marcas

class adminMarcas(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['pk_marcas']
    list_display = ['nike','addidas', 'puma', 'converse']
    resource_class = resourceMarcas

admin.site.register(marcas, adminMarcas)