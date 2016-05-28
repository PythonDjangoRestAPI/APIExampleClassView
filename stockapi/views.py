# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from models import Stock
from serializers import StockSerializer


class stocklist(APIView):
    def get(self, request):
        stocks = Stock.objects.all()
        serializers = StockSerializer(stocks, many=True)
        return Response(serializers.data)

    def post(self):
        pass
