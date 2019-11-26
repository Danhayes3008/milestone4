from django.db import models

class Projects(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    target = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.ImageField(upload_to='images')
    AddressLine1 = models.CharField(max_length=50, default='')
    AddressLine2 = models.CharField(max_length=50, default='')
    town_or_city = models.CharField(max_length=50, default='')
    county = models.CharField(max_length=50, default='')
    country = models.CharField(max_length=50, default='')
    postcode = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.name
