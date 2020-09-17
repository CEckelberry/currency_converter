from unittest import TestCase
from app import app
from flask import session
from forex_python.converter import CurrencyRates, CurrencyCodes
from currency import CurrencyChecks

c = CurrencyRates(force_decimal=False)
cc = CurrencyCodes()


class FlaskTests(TestCase):
    def setUp(self):
        """Stuff to do before every test."""
        self.client = app.test_client()
        app.config["TESTING"] = True

    def test_home(self):
        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<div class="card-body px-lg-5 pt-0">', html)

    def test_dollar_conversion(self):
        with self.client as client:
            self.assertEqual(c.convert("USD", "USD", 1), 1)
            self.assertEqual(c.convert("GBP", "GBP", 1), 1)
            self.assertEqual(c.convert("JPY", "JPY", 1), 1)
