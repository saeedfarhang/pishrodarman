from django.contrib import admin
from . import models
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Cart

admin.site.register(models.Cart, CartAdmin)