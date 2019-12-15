from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=254, default='')
    gender = models.CharField(max_length=6, default='')
    nationality = models.CharField(max_length=100, default='')
    birthday=models.DateField(auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.Profile
