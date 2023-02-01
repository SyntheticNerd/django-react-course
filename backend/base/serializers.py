from rest_framework import serializers
from django.contrib.auth.models import UserManager
from .models import Product, product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
