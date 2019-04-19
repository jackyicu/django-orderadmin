import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Country, Client, Currency, Order, Category, Product, Cart, Shipment, PaymentTerm, Payment

class CountryModelTests(TestCase):
    def test_