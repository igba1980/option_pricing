from django.db import models


class MarketData(models.Model):
    date = models.DateField(auto_now_add=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
