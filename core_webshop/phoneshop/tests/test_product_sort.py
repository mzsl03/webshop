from django.test import TestCase, RequestFactory
from django.urls import reverse
from phoneshop.models import Products
from support_files.sorting import sort_product

class SortProductTests(TestCase):
    def setUp(self):
        self.rf = RequestFactory()
        self.p1 = Products.objects.create(name="Samsung Galaxy A55", category="Telefon", price=169999)
        self.p2 = Products.objects.create(name="Samsung Galaxy S24 Ultra", category="Telefon", price=569999)
        self.p3 = Products.objects.create(name="iPhone 16", category="Telefon", price=354999)
        self.p4 = Products.objects.create(name="iPhone 14 Plus bőrtok magsafe", category="Tartozék", price=213)
        self.p5 = Products.objects.create(name="Vezeték nélküli töltő", category="Tartozék", price=9990)
        self.products = [self.p1, self.p2, self.p3, self.p4, self.p5]

    def make_request(self, params=None):
        params = params or {}
        return self.rf.get("/dummy/", data=params)

    def test_no_filters_returns_all(self):
        req = self.make_request()
        result, categories, filters = sort_product(req, list(self.products))
        self.assertCountEqual(result, self.products)
        self.assertSetEqual(set(categories), {"Telefon", "Tartozék"})
        self.assertEqual(filters, {"name": None, "category": None, "min_price": None, "max_price": None})

    def test_name_filter_case_and_space_insensitive(self):
        req = self.make_request({"name": "  galaxy s24  "})
        result, _, _ = sort_product(req, list(self.products))
        self.assertEqual(result, [self.p2])

    def test_name_substring_matches_multiple(self):
        req = self.make_request({"name": "iphone"})
        result, _, _ = sort_product(req, list(self.products))
        self.assertCountEqual(result, [self.p3, self.p4])

    def test_category_filter_exact(self):
        req = self.make_request({"category": "Tartozék"})
        result, _, _ = sort_product(req, list(self.products))
        self.assertCountEqual(result, [self.p4, self.p5])

    def test_category_all_does_not_filter(self):
        req = self.make_request({"category": "all"})
        result, _, _ = sort_product(req, list(self.products))
        self.assertCountEqual(result, self.products)

    def test_min_price_inclusive(self):
        req = self.make_request({"minPrice": "354999"})
        result, _, _ = sort_product(req, list(self.products))
        self.assertCountEqual(result, [self.p2, self.p3])

    def test_max_price_inclusive(self):
        req = self.make_request({"maxPrice": "213"})
        result, _, _ = sort_product(req, list(self.products))
        self.assertEqual(result, [self.p4])

    def test_min_and_max_price_range(self):
        req = self.make_request({"minPrice": "9000", "maxPrice": "20000"})
        result, _, _ = sort_product(req, list(self.products))
        self.assertEqual(result, [self.p5])

    def test_combined_filters_name_category_price(self):
        req = self.make_request({"name": "iphone", "category": "Telefon", "minPrice": "300000", "maxPrice": "360000"})
        result, _, _ = sort_product(req, list(self.products))
        self.assertEqual(result, [self.p3])

    def test_invalid_price_raises_value_error(self):
        req = self.make_request({"minPrice": "abc"})
        with self.assertRaises(ValueError):
            sort_product(req, list(self.products))
