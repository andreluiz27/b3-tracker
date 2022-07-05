from django.contrib import admin

from .models import StockTracker, StockDomain

class StockTrackerAdmin(admin.ModelAdmin):
    model = StockTracker
    list_display = [field.name for field in StockTracker._meta.get_fields()]

    
admin.site.register(StockTracker, StockTrackerAdmin)
admin.site.register(StockDomain)