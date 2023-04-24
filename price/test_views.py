import pytest
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from price.factories import MarketDataFactory
import arrow


@pytest.mark.django_db
def test_price_list():
    dt = arrow.now().date()
    price_num = '100.20'
    mk_data = MarketDataFactory.create(date=dt, price=price_num)
    client = APIClient()
    response = client.get(reverse('price-list'))

    expected_date = [
        {
            "id": mk_data.pk,
            "date": str(dt),
            "price": price_num
        }
    ]

    assert response.status_code == status.HTTP_200_OK
    data = response.data
    assert len(data) == 1
    assert expected_date == data


@pytest.mark.django_db
def test_price_details():
    dt = arrow.now().date()
    price_num = '100.20'
    price_num2 = '300.20'
    mk_data = MarketDataFactory.create(date=dt, price=price_num)
    mk_data2 = MarketDataFactory.create(date=dt, price=price_num2)
    client = APIClient()
    response = client.get(reverse('price-detail', kwargs={'pk': mk_data.pk}))

    assert response.status_code == status.HTTP_200_OK
    data = response.data
    assert data['id'] == mk_data.pk
