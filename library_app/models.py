from django.db import models
from django.contrib.auth.models import User
# from django.contrib import auth_user

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    borrowed_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    availabilty = models.BooleanField(default=True)
    description = models.TextField(max_length= 100)

    def __str__(self):
        return self.name
    

