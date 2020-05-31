from django.db import models

# Create your models here.
class Product(models.Model):
    persian_name = models.CharField(max_length=150)
    english_name = models.CharField(max_length = 150)
    detail = models.TextField()
    category = models.ForeignKey('products_category',on_delete=models.CASCADE,related_name='+')
    reccomend = models.BooleanField(default=False)
    price = models.PositiveIntegerField(default=0)
    backgroundcolor = models.CharField(max_length=6 , default='F75940')
    image = models.ImageField(default='products/default.png', upload_to='products')
    image_alt=models.CharField(default="image" ,max_length=50)
    date = models.DateTimeField(auto_now_add=False,auto_now = True)
    slug = models.SlugField(default='test')

    # brands
    def __str__(self):
        return self.persian_name
    def snippet(self):
        return self.detail[:50]+"..."

    def cltohex(self):
        return "#" + self.backgroundcolor

class products_category(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(default='categoty/default.png', upload_to='category', max_length=300)
    def __str__(self):
        return self.title
