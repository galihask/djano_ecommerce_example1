from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Product, Cart, Category


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        depth = 1

    def save(self):
        cart = Cart(
            user=self.instance,
            products_ids=self.validated_data['products_ids']
        )
        cart.save()
        return cart


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields=['_id', 'name', 'description', 'created_at', 'last_updated_at']
        fields = '__all__'
        depth = 1

    def save(self):
        product = Product(
            name=self.validated_data['name'],
            description=self.validated_data['description']
        )
        product.save()
        return product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
        depth = 0

    def save(self):
        category = Category(
            name=self.validated_data['name']
        )
        category.save()
        return category



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'first_name',
            'last_name'
        )

        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user




