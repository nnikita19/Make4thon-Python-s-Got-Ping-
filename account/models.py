from django.db import models

# Create your models here.

class person(models.Model):
    username = models.TextField(max_length=30)
    firstname = models.TextField(max_length=30)
    lastname = models.TextField(max_length=30)
    email = models.EmailField()
