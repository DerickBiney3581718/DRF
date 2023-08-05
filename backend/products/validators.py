from rest_framework import serializers
from .models import Product

def validate_title(self, value):
    qs = Product.object.filter(title__iexact= value)
    if qs.exist():
        raise serializers.ValidationError("Need unique title")
    return value