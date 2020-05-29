from django.db import models
from home.models import Product

# Create your models here.
class Cart(models.Model):
    products = models.ManyToManyField(Product , null = True , blank = True)
    total = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=False,auto_now = True)
    def __str__(self):
        return "Cart id: %s" %(self.id)