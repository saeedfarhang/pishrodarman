from django.contrib import admin
from . import models

# Register your models here.


# admin.site.register(models.Products)
admin.site.register(models.products_category)

@admin.register(models.Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('persian_name','english_name','reccomend')
