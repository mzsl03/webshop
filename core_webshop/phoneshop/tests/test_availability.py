from django.test import TestCase
from phoneshop.models import Products, Specs, Shops
from support_files.availability import list_index, list_index_for_accessories
from django.core.exceptions import ObjectDoesNotExist

class AvailabilityUtilsTest(TestCase):
    def setUp(self):
        self.shop = Shops.objects.create(name="Test Shop")
        self.product = Products.objects.create(
            name="Iphone Test",
            category="Telefon",
            price=100000,
            colors=["Black", "White"]
        )
        self.specs = Specs.objects.create(
            product=self.product,
            weight=150,
            battery=3000,
            release_date="2023-01-01",
            storage=[64, 128]
        )

        self.accessory = Products.objects.create(
            name="Iphone Tok",
            category="Tartozék",
            price=10000,
            colors=["Red", "Blue"]
        )

    def test_list_index_returns_correct_index(self):

        index = list_index(self.product.id, "Black", 64)
        self.assertEqual(index, 0)


        index = list_index(self.product.id, "White", 128)
        self.assertEqual(index, 3)

    def test_list_index_for_accessories_returns_correct_index(self):

        index = list_index_for_accessories(self.accessory.id, "Red")
        self.assertEqual(index, 0)


        index = list_index_for_accessories(self.accessory.id, "Blue")
        self.assertEqual(index, 1)

    def test_list_index_raises_value_error_for_invalid_values(self):

        with self.assertRaises(ValueError):
            list_index(9999, "Black", 64)


        with self.assertRaises(ValueError):
            list_index(self.product.id, "Green", 64)


        with self.assertRaises(ValueError):
            list_index(self.product.id, "Black", 256)
