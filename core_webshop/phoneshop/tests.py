from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from phoneshop.models import Users, Workers, Shops, Cart, Products, Specs
from unittest.mock import patch

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


class AddToCartTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.add_url = lambda pid: reverse('add_to_cart', args=[pid])
        cls.cart_url = reverse('user_cart')
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
            colors=['Black', 'Silver'],
            image_path=['/media/phone.jpg'],
            available=[64, 128]
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
            memory=['8GB', '12GB'],
            storage=['64', '128'],
            os='Android 13',
            charge='Fast Charge 25W',
            sensors='Fingerprint, Accelerometer',
            size='160x75x8 mm',
            weight=190,
            battery=5000,
            release_date=date(2023, 9, 1)
        )

    def login(self):
        self.client.login(username='user', password='userpass')

    @patch('phoneshop.views.increment_cart_item', return_value=False)
    def test_add_to_cart_creates_item(self, mock_increment):
        self.login()
        response = self.client.get(self.add_url(self.product.id), {
            'color': 'Black',
            'storage': '64'
        })
        self.assertRedirects(response, self.cart_url)
        cart_item = Cart.objects.get(user=self.profile, product=self.product)
        self.assertEqual(cart_item.quantity, 1)
        self.assertEqual(cart_item.color, 'Black')
        self.assertEqual(cart_item.storage, 64)

    @patch('phoneshop.views.increment_cart_item', return_value=True)
    def test_add_to_cart_does_not_duplicate(self, mock_increment):
        self.login()
        Cart.objects.create(
            user=self.profile,
            product=self.product,
            shop=self.shop,
            quantity=1,
            price=self.product.price,
            color='Black',
            storage=64
        )
        response = self.client.get(self.add_url(self.product.id), {
            'color': 'Black',
            'storage': '64'
        })
        self.assertRedirects(response, self.cart_url)
        self.assertEqual(Cart.objects.filter(user=self.profile, product=self.product).count(), 1)

    def test_invalid_color_returns_400(self):
        self.login()
        response = self.client.get(self.add_url(self.product.id), {
            'color': 'Pink',
            'storage': '64'
        })
        self.assertEqual(response.status_code, 400)

    def test_missing_storage_for_phone_returns_400(self):
        self.login()
        response = self.client.get(self.add_url(self.product.id), {
            'color': 'Black'
        })
        self.assertEqual(response.status_code, 400)

    def test_non_phone_category_allows_missing_storage(self):
        self.login()
        accessory = Products.objects.create(
            name='Case',
            price=5000,
            category='Tartozék',
            colors=['Red'],
            image_path=[],
            available=[]
        )
        response = self.client.get(self.add_url(accessory.id), {
            'color': 'Red'
        })
        self.assertRedirects(response, self.cart_url)
        self.assertTrue(Cart.objects.filter(user=self.profile, product=accessory).exists())

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


if __name__ == '__main__':
    CartViewTests()
    DeleteCartItemTests()
    AddToCartTests()

