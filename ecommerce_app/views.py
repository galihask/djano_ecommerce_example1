from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Product, Cart, Category
from .serializers import ProductSerializer, UserSerializer, CartSerializer, CategorySerializer
from django.db import IntegrityError


@api_view(['GET', 'POST'])
def products(request):
    if request.method == 'POST':
        new_product = ProductSerializer(data=request.data)
        if new_product.is_valid():
            new_product.save()
            return Response(data=new_product.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=new_product.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['PATCH'])
def product(request):
    if request.method == 'PATCH':
        product = Product.objects.get(_id=request.data['_id'])
        product.name = request.data['name']
        product.image = request.data['image']
        product.description = request.data['description']
        product.brand = request.data['brand']
        product.category = request.data['category']
        product.price = request.data['price']
        product.countInStock = request.data['countInStock']
        product.rating = request.data['rating']
        product.numReviews = request.data['numReviews']
        product.save()
        return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def register(request):
    print('method: ',request.method)
    print('data:', request.data)
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(status=status.HTTP_201_CREATED, data=serializer.data)
            except IntegrityError as ex:
                print(ex)
                return Response(status=status.HTTP_409_CONFLICT, data={"message": "email is taken"})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Details are incorrect'})
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data={'message': 'Method not allowed'})


@api_view(['GET', 'POST', 'PATCH'])
def cart(request):
    user = request.user
    # or:
    # we request.user does not work, we can just get the emal of the user in the request
    # and then get it regularly.
    if request.method == 'POST':
        cartSerializer = CartSerializer(instance=user, data=request.data, partial=True)
        if cartSerializer.is_valid():
            cartSerializer.save()
            return Response(status=status.HTTP_201_CREATED, data=cartSerializer.data)

    if request.method == 'PATCH':
        cartSerializer = CartSerializer(instance=request.user, data=request.data, partial=True)
        if cartSerializer.is_valid():
            cartSerializer.save()
            return Response(status=status.HTTP_200_OK, data=cartSerializer.data)

    if request.method == 'GET':
        cartSerializer=CartSerializer(Cart.objects.get(user_id=user))
        return Response(cartSerializer.data)

@api_view(['GET'])
def categories(request):
    if request.method == 'GET':
        categorySerializer = CategorySerializer(Category.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=categorySerializer.data)



