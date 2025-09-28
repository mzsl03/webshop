from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from phoneshop.models import Workers, Shops, Users

class RegisterViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.register_url = reverse('register_worker')
        cls.home_url = reverse('home')

        cls.shop = Shops.objects.create(name="Westend", location="Budapest")

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

    def test_get_register_page_as_superuser(self):
        self.login_as_superuser()
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register_worker.html')

    def test_redirect_if_not_superuser(self):
        self.login_as_normal_user()
        response = self.client.get(self.register_url)
        self.assertRedirects(response, self.home_url)

    def test_successful_registration_creates_records(self):
        self.login_as_superuser()
        response = self.client.post(self.register_url, data=self.valid_form_data)

        self.assertRedirects(response, self.home_url)
        self.assertTrue(User.objects.filter(username='newuser').exists())
        self.assertTrue(Workers.objects.filter(last_name='Kovacs').exists())

        new_user = User.objects.get(username='newuser')
        self.assertTrue(Users.objects.filter(user=new_user).exists())

    def test_registration_invalid_data_does_not_create(self):
        self.login_as_superuser()
        invalid_data = self.valid_form_data.copy()
        invalid_data['email'] = ''

        response = self.client.post(self.register_url, data=invalid_data)
        self.assertEqual(response.status_code, 200)  # újra a form
        self.assertFalse(User.objects.filter(username='newuser').exists())

    def test_registration_requires_login(self):
        response = self.client.get(self.register_url)
        expected_url = f"/?next={self.register_url}"
        self.assertRedirects(response, expected_url)
