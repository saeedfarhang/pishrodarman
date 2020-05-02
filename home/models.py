from django.db import models

# Create your models here.
class Products(models.Model):
    persian_name = models.CharField(max_length=150)
    english_name = models.CharField(max_length = 150)
    ditail = models.TextField()
    category = models.ForeignKey('products_category',on_delete=models.CASCADE,related_name='+',)
    # brands
    # images
    def __str__(self):
        return self.persian_name


class products_category(models.Model):
    title = models.CharField(max_length = 100)
    def __str__(self):
        return self.title
