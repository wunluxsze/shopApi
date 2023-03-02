from django.db import models


class Prod(models.Model):
    name = models.CharField(max_length=200)
    size = models.IntegerField()
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    price = models.IntegerField()


class Category(models.Model):
    name = models.CharField(max_length=200)


class Manufacturer(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
