from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Resume(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return string representation of our users"""
        return f'{self.firstname} {self.lastname}'
