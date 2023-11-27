# guest/models.py
from django.db import models

class Guest(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    government_id = models.CharField(max_length=15)
    address = models.TextField(max_length=200)
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone_number}"