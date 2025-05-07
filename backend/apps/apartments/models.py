from django.db import models
from ..users.models import User

# Create your models here.

class Apartment(models.Model):
    name = models.CharField(max_length=100, null=False)
    slug = models.CharField(max_length=100, unique=True, null=False, primary_key=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    number_of_rooms = models.IntegerField(null=False)
    square = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    availability = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name