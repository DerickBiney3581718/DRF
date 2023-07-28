from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListCreateAPIView.as_view(), name = 'product-create'), 
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name="product-detail"),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name="product-update"),
    path('<int:pk>/delete/', views.ProductDestroyAPIView.as_view(), name="product-detail"),

]
