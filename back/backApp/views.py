from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Product, Category, Cart, Order, Review
from .serializers import LoginSerializer,ProductSerializer, CategorySerializer, CartSerializer, OrderSerializer, ReviewSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth import logout


@login_required
def is_logged(request):
   return JsonResponse({'is_logged': True if request.user.is_authenticated else False})

def log_out(request):
   logout(request)
   return JsonResponse({'is_logged_out': True if not request.user.is_authenticated else False})

class RegistrationViewSet(viewsets.ModelViewSet):
   serializer_class = UserSerializer
   http_method_names = ['post']

class LoginViewToken(TokenObtainPairView):
   serializer_class = LoginSerializer


class ProductViewSet(viewsets.ModelViewSet):
   queryset = Product.objects.all()
   serializer_class = ProductSerializer
   def get_serializer_context(self):
      return {"request": self.request}

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

