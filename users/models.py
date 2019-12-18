from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    name = models.CharField(max_length=250, blank=True)
    gender = models.CharField(max_length=6, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    birthday=models.DateField(auto_now=False, null=True, blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.name
