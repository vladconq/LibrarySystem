from rest_framework import serializers
from .models import AuthorModel, BookModel, ShelfModel


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = AuthorModel


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = BookModel


class ShelfSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ShelfModel
