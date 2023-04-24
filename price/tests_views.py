import pytest
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from price.factories import MarketDataFactory
from django.test import TestCase


@pytest.mark.django_db
def test_price_list():
    MarketDataFactory.create()
    client = APIClient()
    response = client.get(reverse('price-list'))

    assert response.status_code == status.HTTP_200_OK

    data = response.data
    assert len(data) == 1
    assert data[0]['name'] == 'Acme, Inc.'


def test_pass():
    assert True == 'False'




class FooTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def this_wont_run(self):
        print('Fail')

    # def test_this_will(self):
    #     print 'Win'


