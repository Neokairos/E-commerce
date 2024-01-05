from rest_framework import serializers
from .models import Category, Product, Cart, Order, Review
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate, login

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
       model = User
       fields = ['username','password']

    def create(self,validated_data):
        user = User.objects.create_user(validated_data['username'],validated_data['password'])
        login(self.context.get('request'), user)
        return {'username': user.username}

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    category = CategorySerializer()
    seller = UserSerializer()
    
    class Meta:
        model = Product
        fields = ['id','seller','name','description','price','category','image']
    def get_image(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image.url)
        
 
class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Cart
        fields = ['id','user','products']
        
    def create(self, validated_data):
       user_data = validated_data.pop('user')
       user = User.objects.create(**user_data)
       cart = Cart.objects.create(user=user, **validated_data)
       return cart
        
 
class OrderSerializer(serializers.ModelSerializer):
    cart = CartSerializer()
    user = UserSerializer()

    class Meta:
        model = Order
        fields = ['id','user','cart','address','payment_method']

        
 
class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Review
        fields = ['id','user','product','rating','comment']
        
         
   
class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token = super().get_token(user)

        token['username'] = user.username
        return token