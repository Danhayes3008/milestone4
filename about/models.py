from django.db import models

class total_homeless(models.Model):
    totalHomeless = models.DecimalField(max_digits=9, decimal_places=0)
    totalPopulation = models.DecimalField(max_digits=9, decimal_places=0)
    
    def __str__(self):
        return self.name
