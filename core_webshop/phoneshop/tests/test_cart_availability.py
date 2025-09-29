from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from phoneshop.models import Users, Workers, Shops, Cart, Products, Specs


class CartViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.cart_url = reverse('user_cart')
        cls.home_url = reverse('home')

        # Create shop
        cls.shop = Shops.objects.create(
            name='westend',
            location='Budapest, Váci út 1-3'
        )

        # Create worker
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

        # Create superuser and link profile
        cls.superuser = User.objects.create_superuser(
            username='admin',
            password='adminpass',
            email='admin@example.com'
        )
        Users.objects.create(user=cls.superuser, worker=cls.worker)


        cls.regular_user = User.objects.create_user(
            username='user',
            password='userpass'
        )
        Users.objects.create(user=cls.regular_user, worker=cls.worker)


        cls.ghost_user = User.objects.create_user(
            username='ghost',
            password='ghostpass'
        )

        cls.product = Products.objects.create(
            name='Phone',
            price=200000,
            category='Telefon',
            colors=['Black', 'Silver'],
            image_path=['/media/phone1.jpg'],
            available=[64, 128, 256]
        )

        cls.cart = Cart.objects.create(
            user=cls.regular_user.phoneshop_user,
            product=cls.product,
            shop=cls.shop,
            quantity=1,
            price=10000,
            color='Black'
        )

    def login_as(self, username, password):
        self.client.login(username=username, password=password)

    def test_redirects_superuser_to_home(self):
        self.login_as('admin', 'adminpass')
        response = self.client.get(self.cart_url)
        self.assertRedirects(response, self.home_url)

    def test_renders_cart_for_regular_user(self):
        self.login_as('user', 'userpass')
        response = self.client.get(self.cart_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')
        self.assertIn('user', response.context)
        self.assertEqual(response.context['user'].username, 'user')

    def test_redirects_unauthenticated_users(self):
        response = self.client.get(self.cart_url)
        expected_redirect = f"/?next={self.cart_url}"
        self.assertRedirects(response, expected_redirect)

    def test_user_without_profile(self):
        self.login_as('ghost', 'ghostpass')
        response = self.client.get(self.cart_url)
        self.assertEqual(response.status_code, 404)

    def test_staff_user_access_cart(self):
        staff_user = User.objects.create_user(username='staff', password='staffpass', is_staff=True)
        Users.objects.create(user=staff_user, worker=self.worker)

        self.login_as('staff', 'staffpass')
        response = self.client.get(self.cart_url)
        self.assertEqual(response.status_code, 200)

    def test_empty_cart_renders_without_error(self):
        empty_user = User.objects.create_user(username='empty', password='emptypass')
        Users.objects.create(user=empty_user, worker=self.worker)

        self.client.login(username='empty', password='emptypass')
        response = self.client.get(self.cart_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context['cart_items']), [])

    def test_user_with_deleted_worker(self):
        broken_user = User.objects.create_user(username='broken', password='brokenpass')
        broken_profile = Users.objects.create(user=broken_user, worker=self.worker)
        self.worker.delete()

        self.login_as('broken', 'brokenpass')
        response = self.client.get(self.cart_url)
        self.assertTrue(response.status_code in [500, 404])

    def test_cart_page_contains_product_name(self):
        self.login_as('user', 'userpass')
        response = self.client.get(self.cart_url)
        self.assertContains(response, 'Phone')