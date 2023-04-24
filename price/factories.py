from price.models import MarketData
import factory
from datetime import datetime


class MarketDataFactory(factory.django.DjangoModelFactory):
    date = factory.LazyFunction(datetime.now)

    class Meta:
        model = MarketData
