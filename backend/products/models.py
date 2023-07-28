from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(("title"), max_length=150)
    content = models.TextField(("content"), blank=True, null=True)
    price = models.DecimalField(("price"), max_digits=15, decimal_places=2, default=99.99)

    @property    
    def sale_price(self):
        return "{:.2f}".format(float(self.price) * 0.8)
    
    def get_discount(self):
        return "{:.2f}".format(float(self.price) * 0.8)
