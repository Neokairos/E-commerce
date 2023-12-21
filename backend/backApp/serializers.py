from rest_framework import serializers
from .models import Category, Product, Cart, Order, Review

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','description','price','category','image']
        
 
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id','user','products']
        
 
class OrderSerializer(serializers.ModelSerializer):
    cart = CartSerializer()
    class Meta:
        model = Order
        fields = ['id','user','cart','address','payment_method']

        
 
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','user','product','rating','comment']
        
         
   