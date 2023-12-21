from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Product, Category, Cart, Order, Review
from .serializers import ProductSerializer, CategorySerializer, CartSerializer, OrderSerializer, ReviewSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated

class ProductViewSet(viewsets.ModelViewSet):
   queryset = Product.objects.all()
   serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer

class CartViewSet(viewsets.ModelViewSet):
   queryset = Cart.objects.all()
   serializer_class = CartSerializer

class OrderViewSet(viewsets.ModelViewSet):
   queryset = Order.objects.all()
   serializer_class = OrderSerializer

class ReviewViewSet(viewsets.ModelViewSet):
   queryset = Review.objects.all()
   serializer_class = ReviewSerializer

class UserViewSet(viewsets.ModelViewSet):
   permission_classes = [IsAuthenticated]
   queryset = User.objects.all()
   serializer_class = UserSerializer
