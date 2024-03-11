from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Vendor)
admin.site.register(models.ProductCategory)
admin.site.register(models.Product)
admin.site.register(models.SpeciesCategory)
admin.site.register(models.Species)
admin.site.register(models.Races)
admin.site.register(models.Food)
admin.site.register(models.Inventory)
admin.site.register(models.Orders)
admin.site.register(models.ProductDetail)
