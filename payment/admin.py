from django.contrib import admin
from .models import DonationsLineItem, Donation

# Register your models here.
class DonationsLineAdminInline(admin.TabularInline):
    model = DonationsLineItem
    
class DonationsAdmin(admin.ModelAdmin):
    inlines = (DonationsLineAdminInline, )
    
admin.site.register(Donation, DonationsAdmin)