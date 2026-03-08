from django.test import TestCase, Client
from django.contrib.auth.models import User
from decimal import Decimal
from .models import Category, Product, Cart, CartItem, Order, OrderItem


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Electronics',
            description='Phones and Gadgets'
        )

    def test_category_created(self):
        self.assertEqual(self.category.name, 'Electronics')

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Electronics')


class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Electronics')
        self.product = Product.objects.create(
            name='Test Phone',
            description='A test phone',
            category=self.category,
            price=Decimal('10000.00'),
            original_price=Decimal('15000.00'),
            stock=10
        )

    def test_product_created(self):
        self.assertEqual(self.product.name, 'Test Phone')

    def test_product_str(self):
        self.assertEqual(str(self.product), 'Test Phone')

    def test_discount_percentage(self):
        self.assertEqual(self.product.get_discount_percentage(), 33)

    def test_no_discount_when_no_original_price(self):
        self.product.original_price = None
        self.assertEqual(self.product.get_discount_percentage(), 0)

    def test_product_in_stock(self):
        self.assertTrue(self.product.stock > 0)


class CartModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass1234')
        self.category = Category.objects.create(name='Electronics')
        self.product = Product.objects.create(
            name='Test Phone',
            description='A test phone',
            category=self.category,
            price=Decimal('10000.00'),
            stock=5
        )
        self.cart = Cart.objects.create(user=self.user)
        self.cart_item = CartItem.objects.create(
            cart=self.cart,
            product=self.product,
            quantity=2
        )

    def test_cart_total(self):
        self.assertEqual(self.cart.get_total(), Decimal('20000.00'))

    def test_cart_item_total(self):
        self.assertEqual(self.cart_item.get_total(), Decimal('20000.00'))

    def test_cart_str(self):
        self.assertEqual(str(self.cart), 'Cart - testuser')


class StoreViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='pass1234')
        self.category = Category.objects.create(name='Electronics')
        self.product = Product.objects.create(
            name='Test Phone',
            description='A test phone',
            category=self.category,
            price=Decimal('10000.00'),
            stock=5
        )

    def test_home_page_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_loads(self):
        response = self.client.get(f'/product/{self.product.id}/')
        self.assertEqual(response.status_code, 200)

    def test_login_page_loads(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_register_page_loads(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_cart_requires_login(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 302)  # redirect to login
