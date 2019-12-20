from django.contrib import admin
from .models import DonationsLineItem, Donations

# Register your models here.
class DonationsLineAdminInline(admin.TabularInline):
    model = DonationsLineItem
    
class DonationsAdmin(admin.ModelAdmin):
    inlines = (DonationsLineAdminInline, )
    
admin.site.register(Donations, DonationsAdmin)