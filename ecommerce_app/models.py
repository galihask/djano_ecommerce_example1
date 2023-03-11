from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    _id = models.IntegerField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=64, null=False, blank=False)
    image = models.CharField(max_length=256, null=True, blank=False)
    description = models.CharField(max_length=256, null=False, blank=False)
    brand = models.CharField(max_length=256, null=True, blank=False)
    price = models.FloatField(null=True, blank=False)
    countInStock = models.IntegerField(null=True, blank=False)
    rating = models.FloatField(null=True, blank=False)
    numReviews = models.IntegerField(null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=False)
    last_updated_at = models.DateTimeField(auto_now=True, null=True, blank=False)
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self._id}: {self.name}"


class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)


class ProductCart(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    cart_id = models.ForeignKey(Cart, on_delete=models.PROTECT)





