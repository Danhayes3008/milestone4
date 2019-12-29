from django.db import models
from projects.models import Donations

# Create your models here.
class Donation(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    streetadress1 = models.CharField(max_length=40, blank=False)
    streetaddress2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
        
class DonationsLineItem(models.Model):    
    donation = models.ForeignKey(Donation, null=False)
    donations = models.ForeignKey(Donations, null=False)    
    quantity = models.IntegerField(blank=False)
    
    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.donations.name, self.donations.price)