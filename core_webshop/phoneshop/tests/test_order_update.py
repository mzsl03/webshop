import json
from django.test import SimpleTestCase, RequestFactory
from unittest.mock import patch, MagicMock
from phoneshop.views import update_order
from phoneshop.models import Orders as OrdersModel
from unittest.mock import patch

class UpdateOrderBasicTests(SimpleTestCase):
    def setUp(self):
        self.rf = RequestFactory()
        self.choices = [("feldolgozás_alatt", ""), ("kiszállítva", ""), ("törölve", "")]
        self.user = MagicMock(is_authenticated=True)

    def test_invalid_method(self):
        req = self.rf.get("/orders/1/")
        req.user = self.user
        resp = update_order(req, 1)
        self.assertEqual(resp.status_code, 400)

    from phoneshop.models import Orders as OrdersModel
    from unittest.mock import patch

    def test_order_not_found(self):
        req = self.rf.post(
            "/orders/1/",
            data=json.dumps({"status": "kiszállítva"}),
            content_type="application/json",
        )
        req.user = self.user

        with patch("phoneshop.views.Orders.objects.get", side_effect=OrdersModel.DoesNotExist):
            resp = update_order(req, 1)

        self.assertEqual(resp.status_code, 404)
        self.assertJSONEqual(resp.content, {"success": False, "error": "Order not found"})

    def test_same_status_returns_success(self):
        req = self.rf.post("/orders/1/", data=json.dumps({"status": "kiszállítva"}), content_type="application/json")
        req.user = self.user
        with patch("phoneshop.views.Orders") as Orders, patch("phoneshop.views.reverse", return_value="/home/"):
            Orders.status_choices = self.choices
            order = MagicMock()
            order.status = "kiszállítva"
            Orders.objects.get.return_value = order
            resp = update_order(req, 1)
            self.assertEqual(resp.status_code, 200)
            self.assertJSONEqual(resp.content, {"success": True})

    def test_delete_when_torolve(self):
        req = self.rf.post("/orders/1/", data=json.dumps({"status": "törölve"}), content_type="application/json")
        req.user = self.user
        with patch("phoneshop.views.Orders") as Orders, patch("phoneshop.views.reverse", return_value="/home/"):
            Orders.status_choices = self.choices
            order = MagicMock()
            order.status = "feldolgozás_alatt"
            order.product = MagicMock()
            Orders.objects.get.return_value = order
            resp = update_order(req, 1)
            self.assertEqual(resp.status_code, 200)
            order.delete.assert_called_once()

    def test_restock_phone(self):
        req = self.rf.post("/orders/1/", data=json.dumps({"status": "kiszállítva"}), content_type="application/json")
        req.user = self.user
        with patch("phoneshop.views.Orders") as Orders, \
             patch("phoneshop.views.list_index", return_value=1), \
             patch("phoneshop.views.reverse", return_value="/home/"):
            Orders.status_choices = self.choices
            product = MagicMock()
            product.category = "Telefon"
            product.available = [0, 2, 0]
            order = MagicMock()
            order.status = "feldolgozás_alatt"
            order.product = product
            order.color = "black"
            order.storage = 128
            order.quantity = 3
            Orders.objects.get.return_value = order
            resp = update_order(req, 1)
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(product.available[1], 5)

    def test_restock_accessory(self):
        req = self.rf.post("/orders/1/", data=json.dumps({"status": "kiszállítva"}), content_type="application/json")
        req.user = self.user
        with patch("phoneshop.views.Orders") as Orders, \
             patch("phoneshop.views.list_index_for_accessories", return_value=0), \
             patch("phoneshop.views.reverse", return_value="/home/"):
            Orders.status_choices = self.choices
            product = MagicMock()
            product.category = "Kiegeszito"
            product.available = [1, 1]
            order = MagicMock()
            order.status = "feldolgozás_alatt"
            order.product = product
            order.color = "red"
            order.storage = None
            order.quantity = 2
            Orders.objects.get.return_value = order
            resp = update_order(req, 1)
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(product.available[0], 3)

    def test_missing_status_in_body_returns_400(self):
        req = self.rf.post("/orders/1/", data=json.dumps({"x": "y"}), content_type="application/json")
        req.user = self.user
        with patch("phoneshop.views.Orders") as Orders:
            Orders.status_choices = self.choices
            order = MagicMock()
            order.status = "feldolgozás_alatt"
            Orders.objects.get.return_value = order
            resp = update_order(req, 1)
            self.assertEqual(resp.status_code, 400)

    def test_invalid_json_returns_400(self):
        req = self.rf.post("/orders/1/", data="{bad json", content_type="application/json")
        req.user = self.user
        resp = update_order(req, 1)
        self.assertEqual(resp.status_code, 400)

    def test_invalid_status_value_returns_400(self):
        req = self.rf.post("/orders/1/", data=json.dumps({"status": "ismeretlen"}), content_type="application/json")
        req.user = self.user
        with patch("phoneshop.views.Orders") as Orders:
            Orders.status_choices = self.choices
            order = MagicMock()
            order.status = "feldolgozás_alatt"
            Orders.objects.get.return_value = order
            resp = update_order(req, 1)
            self.assertEqual(resp.status_code, 400)

    def test_saves_and_redirects_on_success(self):
        req = self.rf.post("/orders/1/", data=json.dumps({"status": "kiszállítva"}), content_type="application/json")
        req.user = self.user
        with patch("phoneshop.views.Orders") as Orders, \
             patch("phoneshop.views.list_index", return_value=0), \
             patch("phoneshop.views.reverse", return_value="/home/"):
            Orders.status_choices = self.choices
            product = MagicMock()
            product.category = "Telefon"
            product.available = [2]
            order = MagicMock()
            order.status = "feldolgozás_alatt"
            order.product = product
            order.color = "black"
            order.storage = 64
            order.quantity = 1
            Orders.objects.get.return_value = order
            resp = update_order(req, 1)
            self.assertEqual(resp.status_code, 200)