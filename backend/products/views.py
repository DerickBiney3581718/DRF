from django.shortcuts import render, get_object_or_404, Http404
from rest_framework import generics, mixins 
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.permissions import IsStaffEditorPermission
from api.mixins import StaffEditorPermissionMixin
from api.authentication import TokenAuthentication

from .models import Product
from .serializers import ProductSerializer

# Create your views here.


class ProductDetailAPIView(StaffEditorPermissionMixin, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
# lookup_field = 'pk'| default


class ProductUpdateAPIView(StaffEditorPermissionMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class ProductDestroyAPIView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
    #     if not instance.content:
    #         instance.content = instance.title


class ProductListCreateAPIView(StaffEditorPermissionMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]   #Django Model Permissions doesn't include one for view_'model', GET is freee

    def perform_create(self, serializer):
        print(serializer.validated_data)
        # serializer.save(user = self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)


class ProductMixinView(
        StaffEditorPermissionMixin,
        mixins.ListModelMixin,
        generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs['pk']
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
# Customized function view


@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            # queryset = Product.objects.get(id= pk)
            # check 404's
            queryset = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(queryset, many=False).data
        else:
            queryset = Product.objects.all()
            data = ProductSerializer(queryset, many=True).data
        return Response(data)
    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Http404
