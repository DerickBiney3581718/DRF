from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.response import Response  #replaces JsonResponse
from rest_framework.decorators import api_view  #replaces ??

import json
from products.models import Product
from products.serializers import ProductSerializer

# Create your views here.
@api_view(["POST"]) 
def api_home(request, *args, **kwargs):
                                                            # # request.body
                                                            # body = request.body  #stringified json
                                                            # data = {}
                                                            # try:  #in case no data is passed
                                                            #     data = json.loads(body)
                                                            # except:
                                                            #     pass
                                                            # # THe need for a serializer
                                                            # data['params'] = dict(request.GET)
                                                            # data['headers'] = dict(request.headers)
                                                            # data['content_type'] = request.content_type
    # instance = Product.objects.all().order_by("?").first()
    # if instance:
    #     data = ProductSerializer(instance).data
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(instance)
    return Response(serializer.data)