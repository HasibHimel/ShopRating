from django.db import models


class ShoppingMall(models.Model):
    mall_name = models.CharField(max_length=50)
    estd = models.IntegerField()
    about = models.CharField(max_length=1000)
    mall_rating = models.FloatField(default=0)

    def __str__(self):
        return self.mall_name


class Shop(models.Model):
    shopping_mall = models.ForeignKey(ShoppingMall, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=50)
    age = models.FloatField(default=0)
    type = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    shop_rating = models.FloatField(default=0)


class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    rating = models.FloatField(default=0)

