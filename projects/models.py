from django.db import models

class Donations(models.Model):
    name = models.CharField(max_length=254, default='')
    donation = models.DecimalField(max_digits=9, decimal_places=2, default='1.00')
    price = models.DecimalField(max_digits=9, decimal_places=2, default='1.00')
    target = models.DecimalField(max_digits=9, decimal_places=2, default='1.00')
    
    def __str__(self):
        return self.name