from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, CartViewSet, OrderViewSet, ReviewViewSet, UserViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'cart', CartViewSet)
router.register(r'order', OrderViewSet)
router.register(r'review', ReviewViewSet)
router.register(r'user', UserViewSet)


urlpatterns = []
urlpatterns += router.urls