# Generated by Django 4.1.4 on 2023-01-20 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="brand",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="countInStock",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="numReviews",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="price",
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="rating",
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="last_updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
