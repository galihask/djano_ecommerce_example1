from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('products/', views.products),
    path('product/', views.product),
    path('categories', views.categories),
    path('register/', views.register),
    path('token/', obtain_auth_token),
    path('cart', views.cart)
]
