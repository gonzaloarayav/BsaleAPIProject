from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'
    

class Product(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    url_image = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'
