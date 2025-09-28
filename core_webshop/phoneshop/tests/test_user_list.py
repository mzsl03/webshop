from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from phoneshop.models import Users, Workers, Shops


class UserManagementTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.register_url = reverse('register_worker')
        cls.home_url = reverse('home')
        cls.user_list_url = reverse('user_list')

        cls.shop = Shops.objects.create(name="westend", location="Budapest")

        cls.superuser = User.objects.create_superuser(
            username='admin',
            password='adminpass',
            email='admin@test.com'
        )

        cls.superuser_worker = Workers.objects.create(
            last_name='Admin',
            first_name='User',
            address='Budapest, Fő utca 1',
            birth_date=date(1980, 1, 1),
            phone_number='+3611111111',
            position='uzletvezeto',
            shop=cls.shop,
            admin=True
        )

        cls.superuser_profile = Users.objects.create(
            user=cls.superuser,
            worker=cls.superuser_worker
        )

        cls.normal_user = User.objects.create_user(
            username='user',
            password='userpass',
            email='user@test.com'
        )

        cls.normal_worker = Workers.objects.create(
            last_name='Teszt',
            first_name='Felhasználó',
            address='Budapest, Teszt utca 2',
            birth_date=date(1990, 1, 1),
            phone_number='+3622222222',
            position='ertekesito',
            shop=cls.shop,
            admin=False
        )

        cls.normal_profile = Users.objects.create(
            user=cls.normal_user,
            worker=cls.normal_worker
        )

        cls.valid_form_data = {
            'last_name': 'Kovacs',
            'first_name': 'Bela',
            'address': 'Budapest, Teszt utca 1',
            'birth_date': '1990-01-01',
            'phone_number': '+3612345678',
            'position': 'uzletvezeto',
            'shop': cls.shop.id,
            'username': 'newuser',
            'email': 'newuser@test.com',
            'password': 'Password123'
        }

    def login_as_superuser(self):
        self.client.login(username='admin', password='adminpass')

    def login_as_normal_user(self):
        self.client.login(username='user', password='userpass')

    def test_user_list_visible_for_superuser(self):
        self.login_as_superuser()
        response = self.client.get(self.user_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users_list.html')
        self.assertContains(response, 'user')
        self.assertContains(response, 'admin')

    def test_user_list_requires_login(self):
        response = self.client.get(self.user_list_url)
        self.assertRedirects(response, f"/?next={self.user_list_url}")

    def test_user_list_hidden_for_non_superuser(self):
        login_ok = self.client.login(username='user', password='userpass')
        self.assertTrue(login_ok, "A bejelentkezés sikertelen!")
        response = self.client.get(self.user_list_url)
        self.assertRedirects(response, self.home_url)
