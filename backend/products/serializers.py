from rest_framework import serializers, renderers, parsers
import json
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
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
    
    # Both incoming methods are triggered by serializer.save in views
    def create(self, validated_data):
        return Comment(**validated_data)
    def update(self, instance, validated_data):
        instance.email = self.validated_data.get('email', instance.email)
        instance.content = self.validated_data.get('content', instance.content)
        instance.created = self.validated_data.get('created', instance.created)
        # We should save first if needed for db update
        return instance
    #! if .save itself is overriden; the create and update are ignored?
    # Like so
    def save(self):
        email = self.validated_data['email']
        content = self.validated_data['content']
        # send_email_function(to=email, message=content)
        
    # Serializers validate data like forms do and raise exceptions
    #What if I want to make a specific field validation |
    # //Using validators on fields during declaration could also work
    def validate_email(self, value):
        """
        validating if email is gmail
            """
            # ! if field's required is set to False, Won't work
        if 'gmail' not in value:
            raise serializers.ValidationError('email is not from Google')
        return value
    # object-level validation could be possible if multiple fields would be needed
    def validate(self, data):
        """
        validate if email is in content
        """
        if data['email'] in data['content']:
            raise serializers.ValidationError('email should be cryptic')

# Let's serialize 
serialized_data = CommentSerializer(comment).data
json_out = renderers.JSONRenderer().render(serialized_data)
# json_out is a byte string json | stringified json

import io
# Let's deserialize
data = io.BytesIO(json_out)
python_dict_in = parsers.JSONParser().parse(data)
deserialized_data = CommentSerializer(data=python_dict_in, partial = True)
