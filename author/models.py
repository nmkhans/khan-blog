from django.db import models

# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length = 50)
  bio = models.TextField()
  phone_no = models.IntegerField(max_length = 11)