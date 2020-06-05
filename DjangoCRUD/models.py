from django.db import models


class Person(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    birthday = models.CharField(max_length=50)
