from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import log_out,ProductViewSet, CategoryViewSet, CartViewSet, OrderViewSet, ReviewViewSet,RegistrationViewSet, LoginViewToken, is_logged

router = DefaultRouter()
router.register(r'register', RegistrationViewSet, basename='register')
router.register(r'products', ProductViewSet )
router.register(r'cart', CartViewSet)
router.register(r'order', OrderViewSet)
router.register(r'review', ReviewViewSet)
router.register(r'category', CategoryViewSet)


urlpatterns = [ path('login',LoginViewToken.as_view()),
                path('islogged',is_logged),
                path('logout',log_out,)] 

urlpatterns += router.urls