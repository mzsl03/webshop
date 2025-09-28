from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from phoneshop.models import Products, Shops, Workers, Users, Specs
from django.utils import timezone

class EditSpecsViewTest(TestCase):
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
        self.user_phoneshop = Users.objects.create(user=self.superuser, worker=self.worker)

        self.user = User.objects.create_user(username="user", password="user")
        self.user_worker = Workers.objects.create(
            first_name="Normal",
            last_name="User",
            shop=self.shop,
            address="Some Address",
            birth_date="2000-01-01",
            phone_number="987654321",
            position="Staff",
            admin=False
        )
        self.user_phoneshop_normal = Users.objects.create(user=self.user, worker=self.user_worker)

        self.product = Products.objects.create(
            name="Iphone X",
            category="Telefon",
            price=300000,
            colors=["Black", "White"]
        )

        self.url = reverse("edit_specs", args=[self.product.id])

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn(f"/?next={self.url}", response.url)

    def test_redirect_if_not_superuser(self):
        self.client.login(username="user", password="user")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))

    def test_get_edit_specs_page_as_superuser(self):
        self.client.login(username="admin", password="admin")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "edit_specs.html")
        self.assertIn("form", response.context)
        self.assertIn("product", response.context)

    def test_post_invalid_form_does_not_update_existing_specs(self):
        self.client.login(username="admin", password="admin")

        Specs.objects.create(
            product=self.product,
            weight=100,
            battery=3000,
            release_date=timezone.now(),
            storage=[64]
        )

        response = self.client.post(self.url, {
            "weight": "",
            "battery": "",
            "release_date": "",
            "storage": []
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "edit_specs.html")

    def test_get_creates_specs_if_not_exist(self):
        self.client.login(username="admin", password="admin")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Specs.objects.filter(product=self.product).exists())
