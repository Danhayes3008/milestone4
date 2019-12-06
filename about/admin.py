from django.contrib import admin
from .models import total_homeless, yearly_homeless

admin.site.register(total_homeless)
admin.site.register(yearly_homeless)
