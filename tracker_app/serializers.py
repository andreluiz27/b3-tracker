from rest_framework import serializers


class StockTrackerSeralizer(serializers.Serializer):

    symbol = serializers.CharField(max_length=10)
    interval = serializers.CharField(max_length=7)
