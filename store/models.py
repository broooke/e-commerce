from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    text = models.TextField(max_length=2000)
    image = models.ImageField(blank=True,null=True)
    price = models.FloatField()

    def __str__(self):
        return self.name

    @property
    def get_image(self):
        try:
            url = self.image.url
        except :
            url=''
        return url

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product.name

    @property
    def total_sum(self):
        return self.quantity*self.product.price
    
