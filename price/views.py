from rest_framework import generics
from price.models import MarketData
from price.serializers import MarketDataSerializer


class PriceList(generics.ListCreateAPIView):
    queryset = MarketData.objects.all()
    serializer_class = MarketDataSerializer


class PriceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MarketData.objects.all()
    serializer_class = MarketDataSerializer
