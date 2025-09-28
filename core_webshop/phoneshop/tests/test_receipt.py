from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, timedelta, date
from django.db.models import Sum
from django.utils import timezone

from phoneshop.models import Sales, Products, Shops, Users, Workers


class ReceiptsViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.receipts_url = reverse('receipts')
        cls.delete_url = lambda id: reverse('delete_receipt', args=[id])

        cls.user = User.objects.create_user(username='user', password='testpass')

        cls.product = Products.objects.create(
            name="Iphone 16",
            price=300000,
            category="Telefon",
            colors=["black"],
            image_path=["/media/iphone.jpg"],
            available=[128, 256]
        )

        cls.shop = Shops.objects.create(
            name='westend',
            location='Budapest'
        )

        cls.worker = Workers.objects.create(
            last_name='Teszt',
            first_name='Dolgozó',
            address='Test utca 12',
            birth_date=date(1970, 1, 1),
            phone_number='+36703485481',
            position='uzletvezeto',
            shop=cls.shop,
            admin=False
        )

        cls.users = Users.objects.create(
            user=cls.user,
            worker=cls.worker,
        )

        now = timezone.now()

        cls.sale1 = Sales.objects.create(
            product=cls.product,
            shop=cls.shop,
            user=cls.users,
            costumer_name="Teszt Elek",
            selling_time=now,
            price=10000,
            quantity=1,
            tax_number="1234567890",
            zip_code="1234",
            address="Teszt utca 5.",
            city="Budapest",
            color="Black"
        )

        cls.sale2 = Sales.objects.create(
            product=cls.product,
            shop=cls.shop,
            user=cls.users,
            costumer_name="Teszt Elek",
            selling_time=now,
            price=5000,
            quantity=2,
            tax_number="1234567890",
            zip_code="1234",
            address="Teszt utca 5.",
            city="Budapest",
            color="Black"
        )

        cls.sale3 = Sales.objects.create(
            product=cls.product,
            shop=cls.shop,
            user=cls.users,
            costumer_name="Másik Vevő",
            selling_time=now + timedelta(minutes=5),
            price=20000,
            quantity=1,
            tax_number="9876543210",
            zip_code="5678",
            address="Másik utca 10.",
            city="Debrecen",
            color="Silver"
        )

    def login(self):
        self.client.login(username='user', password='testpass')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(self.receipts_url)
        self.assertRedirects(response, f"/?next={self.receipts_url}")

    def test_receipts_view_with_data(self):
        self.login()
        response = self.client.get(self.receipts_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'receipts.html')

        receipts = response.context['receipts']

        teszt_elek_total = sum(r['total_price'] for r in receipts if r['costumer_name'] == 'Teszt Elek')
        self.assertEqual(teszt_elek_total, 15000)

        other_total = sum(r['total_price'] for r in receipts if r['costumer_name'] == 'Másik Vevő')
        self.assertEqual(other_total, 20000)

    def test_receipts_view_empty(self):
        Sales.objects.all().delete()
        self.login()
        response = self.client.get(self.receipts_url)
        self.assertEqual(list(response.context['receipts']), [])

    def test_delete_receipt_success(self):
        self.login()
        sale_id = self.sale1.id
        response = self.client.post(self.delete_url(sale_id))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"success": True, "deleted": 1})
        self.assertFalse(Sales.objects.filter(id=sale_id).exists())

    def test_delete_receipt_not_found(self):
        self.login()
        response = self.client.post(self.delete_url(99999))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"success": True, "deleted": 0})

    def test_delete_receipt_requires_login(self):
        sale_id = self.sale2.id
        response = self.client.post(self.delete_url(sale_id))
        self.assertRedirects(response, f"/?next={self.delete_url(sale_id)}")

    def test_delete_receipt_server_error(self):
        self.login()
        with self.assertRaises(Exception):
            response = self.client.post(self.delete_url("bad_id"))
            self.assertEqual(response.status_code, 500)
            self.assertIn("error", response.json())
