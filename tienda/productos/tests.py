from django.test import TestCase
from django.urls import reverse
from .models import Producto

class ProductoModelTest(TestCase):
    def setUp(self):
        self.producto = Producto.objects.create(
            nombre="Coca Cola", descripcion="Bebida gaseosa", precio=120.50, stock=10, disponible=True
        )

    def test_str_producto(self):
        self.assertEqual(str(self.producto), "Coca Cola")

    def test_hay_stock_true(self):
        self.assertTrue(self.producto.hay_stock())

    def test_hay_stock_false(self):
        self.producto.stock = 0
        self.assertFalse(self.producto.hay_stock())

class ProductoViewsTest(TestCase):
    def setUp(self):
        self.producto = Producto.objects.create(
            nombre="Pepsi", descripcion="Bebida gaseosa", precio=100.00, stock=0, disponible=False
        )

    def test_lista_productos(self):
        response = self.client.get(reverse('lista_productos'))
        self.assertEqual(response.status_code, 200)
        self.assertIn("Pepsi", str(response.content))

    def test_detalle_producto_ok(self):
        response = self.client.get(reverse('detalle_producto', args=[self.producto.id]))
        self.assertEqual(response.status_code, 200)
        self.assertIn("Pepsi", str(response.content))

    def test_detalle_producto_not_found(self):
        response = self.client.get(reverse('detalle_producto', args=[999]))
        self.assertEqual(response.status_code, 404)