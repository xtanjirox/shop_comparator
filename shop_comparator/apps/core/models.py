from django.db import models
from django.utils import timezone


class Shop(models.Model):
    shop_name = models.CharField(max_length=130)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, null=True)
    deactivated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'shop'


class Product(models.Model):
    product_name = models.CharField(max_length=130)
    product_link = models.CharField(max_length=250)
    unit_price = models.FloatField(default=0)
    promo_price = models.FloatField(default=0)
    shop = models.ForeignKey(Shop, on_delete=models.DO_NOTHING)
    scrap_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    promo_last_date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'product'
