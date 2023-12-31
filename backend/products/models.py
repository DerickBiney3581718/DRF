from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
import random
# Create your models here.
TAGS_MODEL_VALUES = ['electronics', 'cars', 'movies', 'boats']
class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)
    
    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs
# //////////////////////////////////////////////////////////////////
class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)
    
    def search(self, query, user=None):
        return self.get_queryset().is_public().search(query, user)
# /////////////////////////////////////////////////////////////////////////
class Product(models.Model):
    user = models.ForeignKey(User,default=1, null=True,  on_delete= models.SET_NULL)
    title = models.CharField(("title"), max_length=150)
    content = models.TextField(("content"), blank=True, null=True)
    price = models.DecimalField(("price"), max_digits=15, decimal_places=2, default=99.99)
    public = models.BooleanField(default=True)
    objects = ProductManager()
    
    def is_public(self):
        return self.public
    def get_tag_list(self):
        return [random.choice(TAGS_MODEL_VALUES)]
    @property    
    def sale_price(self):
        return "{:.2f}".format(float(self.price) * 0.8)
    
    def get_discount(self):
        return "{:.2f}".format(float(self.price) * 0.8)
