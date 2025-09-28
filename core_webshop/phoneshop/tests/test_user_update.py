from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from phoneshop.models import Users, Workers, Shops

class UpdateUserTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

        cls.register_url = reverse('register_worker')
        cls.user_list_url = reverse('user_list')
        cls.update_url = lambda user_id: reverse('update_user', args=[user_id])
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
            phone_number='+361111111',
            position='uzletvezeto',
            shop=cls.shop,
            admin=True
        )

        cls.superuser_profile = Users.objects.create(
            user=cls.superuser,
            worker=cls.superuser_worker
        )

        # Normál user
        cls.normal_user = User.objects.create_user(
            username='normaluser',
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
        self.client.login(username='normaluser', password='userpass')

    def test_update_user_success(self):
        self.login_as_superuser()
        response = self.client.post(self.update_url(self.normal_user.id), {
            'username': self.normal_user.username,
            'email': self.normal_user.email,
            'first_name': 'Updated',
            'last_name': 'Name'
        })
        self.assertRedirects(response, self.user_list_url)

        self.normal_user.refresh_from_db()
        self.assertEqual(self.normal_user.first_name, 'Updated')
        self.assertEqual(self.normal_user.last_name, 'Name')

    def test_update_user_requires_login(self):
        response = self.client.get(self.update_url(self.normal_user.id))
        self.assertRedirects(response, f"/?next={self.update_url(self.normal_user.id)}")

    def test_update_user_invalid_data(self):
        self.login_as_superuser()
        response = self.client.post(self.update_url(self.normal_user.id), {
            'username': self.normal_user.username,
            'email': ''
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.user_list_url)

        self.normal_user.refresh_from_db()
        self.assertEqual(self.normal_user.email, '')


    def test_update_user_nonexistent_id(self):
        self.login_as_superuser()
        response = self.client.get(self.update_url(99999))
        self.assertEqual(response.status_code, 404)

    def test_update_user_duplicate_username(self):
        self.login_as_superuser()
        another_user = User.objects.create_user(
            username='anotheruser',
            password='pass123',
            email='another@test.com'
        )
        response = self.client.post(self.update_url(self.normal_user.id), {
            'username': 'anotheruser',
            'email': self.normal_user.email
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "felhasználónév")
        self.normal_user.refresh_from_db()
        self.assertNotEqual(self.normal_user.username, 'anotheruser')

    def test_update_user_forbidden_for_non_superuser(self):
        self.login_as_normal_user()
        response = self.client.post(self.update_url(self.superuser.id), {
            'username': 'hacker'
        })
        self.assertEqual(response.status_code, 302)
        self.superuser.refresh_from_db()
        self.assertNotEqual(self.superuser.username, 'hacker')