from django.test import TestCase, Client
from phoneshop.models import Products, Shops, Workers, Users
from django.contrib.auth.models import User 
from django.urls import reverse


class ProductAddNewTest(TestCase):
    def setUp(self):
        self.client = Client()


        self.shop = Shops.objects.create(name="Test Shop")


        self.superuser = User.objects.create_superuser(
            username="admin", email="admin@admin.com", password="admin"
        )

        self.worker = Workers.objects.create(
            first_name="Admin",
            last_name="User",
            shop=self.shop,
            address="Test Address",
            birth_date="2000-01-01",
            phone_number="123456789",
            position="Manager",
            admin=True
        )

        self.phoneshop_user = Users.objects.create(user=self.superuser, worker=self.worker)


        self.user = User.objects.create_user(
            username="user", password="user"
        )

        self.user_worker = Workers.objects.create(
            first_name="Normal",
            last_name="User",
            shop=self.shop,
            address="Test Address",
            birth_date="2000-01-01",
            phone_number="987654321",
            position="Staff",
            admin=False
        )
        self.user_phoneshop = Users.objects.create(user=self.user, worker=self.user_worker)

        self.url = reverse("add_product")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"/?next={self.url}")

    def test_redirect_if_not_superuser(self):
        self.client.login(
            username="user", password="user" 
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    def test_get_add_product_page_as_superuser(self):
        self.client.login(username="admin", password="admin")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "add_product.html")
        self.assertIn("form", response.context)

    def test_post_valid_form_creates_phone_product_and_redirects_to_edit_specs(self):
        self.client.login(username="admin", password="admin")
        response = self.client.post(self.url,{
            "name": "Iphone 9",
            "category": "Telefon",
            "price": 250000,
            "colors": ["Black", "White"]
        })
        self.assertEqual(Products.objects.count(), 1)
        product = Products.objects.first()
        self.assertEqual(product.name, "Iphone 9")
        self.assertEqual(product.category, "Telefon")
        self.assertRedirects(response, reverse("edit_specs", args=[product.id]))
    
    def test_post_valid_form_creates_accessory_product_and_redirects_home(self):
        self.client.login(username="admin", password="admin")
        response = self.client.post(self.url, {
            "name": "Iphone 9 tok",
            "category": "Tartozék",
            "price": 25000,
            "colors": ["Black", "White"]
        })
        self.assertEqual(Products.objects.count(), 1)
        product = Products.objects.first()
        self.assertEqual(product.category, "Tartozék")
        self.assertRedirects(response, reverse("home"))

    def test_post_invalid_form_does_not_create_product(self):
        self.client.login(username="admin", password="admin")
        response = self.client.post(self.url, {
            "name": "",
            "category": "Telefon",
            "price": ""
        })

        self.assertEqual(Products.objects.count(), 0)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "add_product.html")
    
    def test_post_duplicate_product_name_fails(self):
        self.client.login(username="admin", password="admin")
        Products.objects.create(name="Iphone 9", category="Telefon", price=250000)
        response = self.client.post(self.url, {
            "name": "Iphone 9",
            "category": "Telefon",
            "price": 250000,
            "colors": ["Black", "White"]
        })
        self.assertEqual(Products.objects.count(), 1)
        self.assertTemplateUsed(response, "add_product.html")

    def test_cannot_add_duplicate_product_shows_error_message(self):
        self.client.login(username="admin", password="admin")


        Products.objects.create(
            name="Iphone 9",
            category="Telefon",
            price=250000,
            colors=["Black", "White"],
        )


        response = self.client.post(self.url, {
            "name": "Iphone 9",
            "category": "Telefon",
            "price": 250000,
            "colors": ["Black", "White"],
        })


        self.assertEqual(Products.objects.count(), 1)


        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "add_product.html")


        messages = list(response.context["messages"])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Ez a termék már létezik!")
    

