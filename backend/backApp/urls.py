from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, CartViewSet, OrderViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'cart', CartViewSet)
router.register(r'order', OrderViewSet)
router.register(r'review', ReviewViewSet)
##prolly dont need a router for it tho
router.register(r'category', CategoryViewSet)


urlpatterns = [] 
urlpatterns += router.urls