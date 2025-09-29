from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from phoneshop.models import Users, Workers, Shops, Cart, Products, Specs

class DeleteCartItemTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.delete_url = lambda item_id: reverse('delete_cart_item', args=[item_id])
        cls.home_url = reverse('home')

        cls.shop = Shops.objects.create(name='westend', location='Budapest, Váci út 1-3')

        cls.worker = Workers.objects.create(
            last_name='Test',
            first_name='Worker',
            address='123 Test Street',
            birth_date=date(1990, 1, 1),
            phone_number='123456789',
            position='uzletvezeto',
            shop=cls.shop,
            admin=False
        )

        cls.user = User.objects.create_user(username='user', password='userpass')
        cls.profile = Users.objects.create(user=cls.user, worker=cls.worker)

        cls.product = Products.objects.create(
            name='Phone',
            price=200000,
            category='Telefon',
            colors=['Black'],
            image_path=[],
            available=[64]
        )

        cls.specs = Specs.objects.create(
            product=cls.product,
            CPU_speed='3.2 GHz',
            CPU_type='Octa-core',
            display_size='6.5"',
            resolution='2400x1080',
            display_technology='AMOLED',
            max_refresh_rate='120Hz',
            Spen=False,
            camera='108MP',
            memory=['8GB'],
            storage=['64'],
            os='Android 13',
            charge='Fast Charge',
            sensors='Fingerprint',
            size='160x75x8 mm',
            weight=190,
            battery=5000,
            release_date=date(2023, 9, 1)
        )

        cls.cart_item = Cart.objects.create(
            user=cls.profile,
            product=cls.product,
            shop=cls.shop,
            quantity=1,
            price=cls.product.price,
            color='Black',
            storage=64
        )

    def login(self):
        self.client.login(username='user', password='userpass')

    def test_delete_cart_item_success(self):
        self.login()
        response = self.client.post(self.delete_url(self.cart_item.id))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'success': True})
        self.assertFalse(Cart.objects.filter(id=self.cart_item.id).exists())

    def test_delete_cart_item_not_found(self):
        self.login()
        response = self.client.post(self.delete_url(9999))  # non-existent ID
        self.assertEqual(response.status_code, 404)
        self.assertJSONEqual(response.content, {'success': False, 'error': 'Item not found'})

    def test_superuser_redirects_to_home(self):
        superuser = User.objects.create_superuser(username='admin', password='adminpass', email='admin@example.com')
        Users.objects.create(user=superuser, worker=self.worker)
        self.client.login(username='admin', password='adminpass')

        response = self.client.post(self.delete_url(self.cart_item.id))
        self.assertRedirects(response, self.home_url)

    def test_get_request_returns_405(self):
        self.login()
        response = self.client.get(self.delete_url(self.cart_item.id))
        self.assertEqual(response.status_code, 405)