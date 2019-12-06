from django.db import models

class total_homeless(models.Model):
    name = models.CharField(max_length=250, default="")
    totalHomeless = models.DecimalField(max_digits=9, decimal_places=0)
    totalPopulation = models.DecimalField(max_digits=9, decimal_places=0)
    
    def __str__(self):
        return self.name

class yearly_homeless(models.Model):
    name = models.CharField(max_length=250, defaults="")
    year = models.DecimalField(max_digits=4, decimal_places=0)
    total = models.DecimalField(max_digits=9, decimal_places=0)
    
    def __str__(self):
        return self.name