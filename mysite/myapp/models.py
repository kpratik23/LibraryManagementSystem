from django.db import models


# Create your models here.

class Book(models.Model):
    isbn = models.IntegerField(null=True)
    bookname = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=100, null=True)
    publication = models.CharField(max_length=100, null=True)
    quantity = models.IntegerField(null=True)


class Issue(models.Model):
    studentid = models.IntegerField(null=True)
    name = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    rollno = models.CharField(max_length=100)
    issued = models.DateTimeField()
    submitdate = models.DateTimeField(null=True)


class submit(models.Model):
    studentid = models.IntegerField(null=True)
    name = models.CharField(max_length=100, null=True)
    isbn = models.CharField(max_length=100, null=True)
    branch = models.CharField(max_length=100, null=True)
    rollno = models.CharField(max_length=100, null=True)
    issued = models.DateTimeField(null=True)
    submitdate = models.DateTimeField(null=True)
    fine = models.FloatField(null=True)
