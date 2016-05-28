from rest_framework import serializers

from stockapi.models import Stock


# class based view example
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('id', 'ticket', 'open', 'close', 'volume')
