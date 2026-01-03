from django.core.management.base import BaseCommand
from store.models import Product

class Command(BaseCommand):
    help = 'Add sample products to the database'

    def handle(self, *args, **kwargs):
        products = [
            {
                'name': 'Wireless Headphones',
                'description': 'Premium wireless headphones with active noise cancellation. Enjoy crystal-clear audio and up to 30 hours of battery life. Perfect for music lovers and professionals.',
                'price': 199.99,
                'stock': 25,
                'image_url': 'https://example.com/headphones.jpg'
            },
            {
                'name': 'Smart Watch',
                'description': 'Advanced fitness tracking smartwatch with heart rate monitor, GPS, and water resistance. Track your workouts, monitor your health, and stay connected on the go.',
                'price': 299.99,
                'stock': 15,
                'image_url': 'https://example.com/smartwatch.jpg'
            },
            {
                'name': 'Laptop Stand',
                'description': 'Ergonomic aluminum laptop stand with adjustable height. Improve your posture and reduce neck strain while working. Compatible with all laptop sizes.',
                'price': 49.99,
                'stock': 50,
                'image_url': 'https://example.com/laptopstand.jpg'
            },
            {
                'name': 'Mechanical Keyboard',
                'description': 'RGB backlit mechanical gaming keyboard with customizable keys and responsive switches. Perfect for gamers and programmers who demand precision and speed.',
                'price': 129.99,
                'stock': 30,
                'image_url': 'https://example.com/keyboard.jpg'
            },
            {
                'name': 'Wireless Mouse',
                'description': 'Precision wireless mouse with ergonomic design and long battery life. Features adjustable DPI settings and works on any surface.',
                'price': 39.99,
                'stock': 40,
                'image_url': 'https://example.com/mouse.jpg'
            },
            {
                'name': 'USB-C Hub',
                'description': '7-in-1 USB-C hub with HDMI, USB 3.0 ports, SD card reader, and power delivery. Expand your laptop connectivity with this compact adapter.',
                'price': 59.99,
                'stock': 35,
                'image_url': 'https://example.com/usbhub.jpg'
            },
            {
                'name': 'Portable Charger',
                'description': '20000mAh portable power bank with fast charging support. Keep your devices charged on the go with dual USB outputs and LED battery indicator.',
                'price': 44.99,
                'stock': 45,
                'image_url': 'https://example.com/charger.jpg'
            },
            {
                'name': 'Webcam HD',
                'description': '1080p HD webcam with built-in microphone and auto-focus. Perfect for video calls, streaming, and online meetings. Plug and play compatibility.',
                'price': 79.99,
                'stock': 20,
                'image_url': 'https://example.com/webcam.jpg'
            },
            {
                'name': 'Phone Case',
                'description': 'Durable protective phone case with shock absorption and raised edges. Slim design that fits perfectly and protects your device from drops and scratches.',
                'price': 24.99,
                'stock': 100,
                'image_url': 'https://example.com/phonecase.jpg'
            },
            {
                'name': 'Bluetooth Speaker',
                'description': 'Waterproof portable bluetooth speaker with 360-degree sound. Enjoy 12 hours of playtime and deep bass for indoor and outdoor use.',
                'price': 89.99,
                'stock': 28,
                'image_url': 'https://example.com/speaker.jpg'
            },
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults=product_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))

        self.stdout.write(self.style.SUCCESS('\nSample data loaded successfully!'))
