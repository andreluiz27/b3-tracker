"""
Model definition of tracker_app
"""
from django.db import models


class StockTracker(models.Model):
    """

    Fields:
    
    symbol: symbol of stock being tracked (e.g PETR4.SA)
    open_value: open value of tracked stock inside tracker interval
    low_value: lowest value of tracked stock inside tracker interval
    high_value: highest value of tracked stock inside tracker interval
    close_value: close value of tracked stock inside tracker interval
    volume: volume traded of tracked stock inside tracker interval
    dt_time: open value of tracked stock inside tracker interval
    interval: tracker time interval   
    """

    symbol = models.CharField(max_length=10)
    open_value = models.FloatField()
    low_value = models.FloatField()
    high_value = models.FloatField()
    close_value = models.FloatField()
    volume = models.IntegerField()
    dt_time = models.DateTimeField()
    interval = models.CharField(max_length=7)
