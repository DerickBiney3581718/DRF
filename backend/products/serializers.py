from rest_framework import serializers, renderers, parsers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # get_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = ("__all__")
        # def get_my_discount(self, obj):
        # if not hasattr(obj, 'id')
        #     return obj.get_discount()
# Creating an object
from datetime import datetime
class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

comment = Comment(email='sonnydevito@gmail.com', content='We rule the night')

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_lenght=200)
    created = serializers.DateTimeField()
    
# Let's serialize 
