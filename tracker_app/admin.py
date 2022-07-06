from django.contrib import admin

from .models import StockTracker, StockDomain, StockTrigger


class StockTrackerAdmin(admin.ModelAdmin):
    model = StockTracker
    list_display = [
        "symbol",
        "open_value",
        "close_value",
        "high_value",
        "low_value",
        "dt_time",
    ]

class StockDomainAdmin(admin.ModelAdmin):
    model = StockDomain
    list_display = ["company_name","symbol"]

class StockTriggerAdmin(admin.ModelAdmin):
    model = StockTrigger
    list_display = [field.name for field in StockTrigger._meta.get_fields()]


admin.site.register(StockTracker, StockTrackerAdmin)
admin.site.register(StockTrigger, StockTriggerAdmin)
admin.site.register(StockDomain, StockDomainAdmin)
