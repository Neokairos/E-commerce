from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Product(models.Model):
    Seller = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(default="nigga be empty")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')


class Cart(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   products = models.ManyToManyField(Product)

   def __str__(self):
       return f"{self.user.username}'s cart"
   
   
class Order(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
   address = models.CharField(max_length=200)
   payment_method = models.CharField(max_length=200)

   def __str__(self):
       return f"{self.user.username}'s order"

class Review(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   rating = models.IntegerField()
   comment = models.TextField()

   def __str__(self):
       return f"{self.user.username}'s review for {self.product.name}"