from rest_framework import serializers
from .models import Prod


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prod
        fields = "__all__"
