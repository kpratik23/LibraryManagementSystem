from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *


class ListBookSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Book
        fields = ["id", "isbn", "bookname", "author", "publication", "quantity"]


class BookSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Issue
        fields = ["id", "name", "isbn", "branch", "rollno", "issued", "submitdate", "studentid"]


class SubmitBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = submit
        fields = ["studentid", "name", "isbn", "branch", "rollno", "issued", "submitdate", "fine"]
