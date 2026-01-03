from django.core.management.base import BaseCommand
from store.models import Category, Product

class Command(BaseCommand):
    help = 'Add Kenyan market products to the database'

    def handle(self, *args, **kwargs):
        # Get categories
        try:
            audio = Category.objects.get(name='Audio')
            computers = Category.objects.get(name='Computers')
            gaming = Category.objects.get(name='Gaming')
            electronics = Category.objects.get(name='Electronics')
            accessories = Category.objects.get(name='Accessories')
        except Category.DoesNotExist:
            self.stdout.write(self.style.ERROR('Categories not found. Run update_products first.'))
            return

        # Clear existing products
        Product.objects.all().delete()
        self.stdout.write(self.style.WARNING('Cleared existing products'))

        products = [
            # AUDIO CATEGORY - Earbuds/Earphones
            {
                'name': 'Oraimo FreePods 3 TWS Earbuds',
                'description': 'True wireless earbuds with superior sound quality, 20-hour battery life, and IPX5 water resistance. Perfect for workouts and daily use.',
                'category': audio,
                'price': 2499,
                'original_price': 3500,
                'stock': 45,
                'image_url': 'https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=500',
                'is_featured': True
            },
            {
                'name': 'Oraimo AirBuds 2 Wireless Earphones',
                'description': 'Affordable wireless earphones with great bass, built-in mic, and 6-hour playtime. Lightweight and comfortable for all-day wear.',
                'category': audio,
                'price': 1299,
                'original_price': 1800,
                'stock': 60,
                'image_url': 'https://images.unsplash.com/photo-1606841837239-c5a1a4a07af7?w=500',
                'is_featured': False
            },
            {
                'name': 'Samsung Galaxy Buds 2 Pro',
                'description': 'Premium wireless earbuds with active noise cancellation, 360-degree audio, and seamless Samsung device integration.',
                'category': audio,
                'price': 18999,
                'original_price': 24999,
                'stock': 15,
                'image_url': 'https://images.unsplash.com/photo-1629367494173-c78a56567877?w=500',
                'is_featured': True
            },
            {
                'name': 'Apple AirPods Pro (2nd Gen)',
                'description': 'Advanced AirPods with adaptive transparency, personalized spatial audio, and up to 2x more noise cancellation.',
                'category': audio,
                'price': 32999,
                'original_price': 39999,
                'stock': 12,
                'image_url': 'https://images.unsplash.com/photo-1606841837239-c5a1a4a07af7?w=500',
                'is_featured': True
            },
            {
                'name': 'Apple AirPods (3rd Generation)',
                'description': 'Spatial audio with dynamic head tracking, adaptive EQ, and up to 30 hours total listening time with charging case.',
                'category': audio,
                'price': 24999,
                'original_price': 29999,
                'stock': 20,
                'image_url': 'https://images.unsplash.com/photo-1606220588913-b3aacb4d2f46?w=500',
                'is_featured': False
            },
            {
                'name': 'Samsung Galaxy Buds FE',
                'description': 'Fan Edition wireless earbuds with active noise cancelling, great sound quality, and affordable price point.',
                'category': audio,
                'price': 12999,
                'original_price': 16999,
                'stock': 30,
                'image_url': 'https://images.unsplash.com/photo-1598331668521-1f0c82f1c835?w=500',
                'is_featured': False
            },

            # COMPUTERS CATEGORY
            {
                'name': 'HP EliteBook 840 G8 - Intel i5 11th Gen',
                'description': '14" FHD laptop with Intel Core i5-1135G7, 8GB RAM, 256GB SSD. Perfect for business and productivity.',
                'category': computers,
                'price': 65999,
                'original_price': 79999,
                'stock': 8,
                'image_url': 'https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=500',
                'is_featured': True
            },
            {
                'name': 'Dell Inspiron 15 3000 - AMD Ryzen 5',
                'description': '15.6" laptop with AMD Ryzen 5, 8GB RAM, 512GB SSD, Windows 11. Great value for students and home use.',
                'category': computers,
                'price': 54999,
                'original_price': 64999,
                'stock': 12,
                'image_url': 'https://images.unsplash.com/photo-1593642702749-b7d2a804fbcf?w=500',
                'is_featured': True
            },
            {
                'name': 'Lenovo ThinkPad T14 Gen 3 - Intel i7',
                'description': 'Business-class 14" laptop with Intel i7-1255U, 16GB RAM, 512GB SSD. Military-grade durability.',
                'category': computers,
                'price': 98999,
                'original_price': 119999,
                'stock': 5,
                'image_url': 'https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=500',
                'is_featured': False
            },
            {
                'name': 'Dell OptiPlex 7090 Desktop Mini PC',
                'description': 'Compact business desktop with Intel i5-10500T, 8GB RAM, 256GB SSD. Space-saving design with full power.',
                'category': computers,
                'price': 48999,
                'original_price': 59999,
                'stock': 10,
                'image_url': 'https://images.unsplash.com/photo-1587202372634-32705e3bf49c?w=500',
                'is_featured': False
            },
            {
                'name': 'HP Desktop Tower - Intel i3',
                'description': 'Desktop PC with Intel i3-10100, 8GB RAM, 1TB HDD. Perfect for office work and general computing.',
                'category': computers,
                'price': 38999,
                'original_price': 45999,
                'stock': 15,
                'image_url': 'https://images.unsplash.com/photo-1593640408182-31c70c8268f5?w=500',
                'is_featured': False
            },
            {
                'name': 'LG 24" Full HD IPS Monitor',
                'description': '24-inch 1920x1080 IPS display with AMD FreeSync, perfect for productivity and entertainment.',
                'category': computers,
                'price': 15999,
                'original_price': 19999,
                'stock': 25,
                'image_url': 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500',
                'is_featured': False
            },
            {
                'name': 'Dell 27" QHD Monitor - P2722H',
                'description': '27-inch 2560x1440 monitor with USB-C connectivity, height-adjustable stand, perfect for professionals.',
                'category': computers,
                'price': 32999,
                'original_price': 39999,
                'stock': 8,
                'image_url': 'https://images.unsplash.com/photo-1585792180666-f7347c490ee2?w=500',
                'is_featured': True
            },
            {
                'name': 'Logitech C920 HD Pro Webcam',
                'description': '1080p HD webcam with stereo audio, perfect for video calls, streaming, and content creation.',
                'category': computers,
                'price': 8999,
                'original_price': 12999,
                'stock': 30,
                'image_url': 'https://images.unsplash.com/photo-1593642702749-b7d2a804fbcf?w=500',
                'is_featured': False
            },
            {
                'name': 'Original HP Laptop Battery - 4 Cell',
                'description': 'Genuine HP replacement battery for EliteBook and ProBook series. 14.8V, 2800mAh capacity.',
                'category': computers,
                'price': 4999,
                'original_price': 6999,
                'stock': 20,
                'image_url': 'https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=500',
                'is_featured': False
            },
            {
                'name': 'Dell 65W USB-C Laptop Charger',
                'description': 'Universal USB-C power adapter compatible with Dell, HP, and Lenovo laptops. Compact and portable.',
                'category': computers,
                'price': 3499,
                'original_price': 4999,
                'stock': 35,
                'image_url': 'https://images.unsplash.com/photo-1625948515291-69613efd103f?w=500',
                'is_featured': False
            },
            {
                'name': 'HP 90W Smart AC Adapter',
                'description': 'Original HP charger for EliteBook, ProBook, and Pavilion laptops. 4.5mm connector.',
                'category': computers,
                'price': 2999,
                'original_price': 4499,
                'stock': 40,
                'image_url': 'https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=500',
                'is_featured': False
            },
            {
                'name': 'Dell WD19 180W Docking Station',
                'description': 'Universal USB-C docking station with dual display support, ethernet, and multiple USB ports.',
                'category': computers,
                'price': 24999,
                'original_price': 32999,
                'stock': 10,
                'image_url': 'https://images.unsplash.com/photo-1625948515291-69613efd103f?w=500',
                'is_featured': False
            },
            {
                'name': 'Lenovo ThinkPad USB-C Dock Gen 2',
                'description': 'Professional docking solution with dual 4K display support, 90W power delivery.',
                'category': computers,
                'price': 28999,
                'original_price': 35999,
                'stock': 8,
                'image_url': 'https://images.unsplash.com/photo-1625948515291-69613efd103f?w=500',
                'is_featured': False
            },

            # GAMING CATEGORY
            {
                'name': 'Logitech G502 HERO Gaming Mouse',
                'description': 'High-performance gaming mouse with 25,600 DPI sensor, 11 programmable buttons, and RGB lighting.',
                'category': gaming,
                'price': 8999,
                'original_price': 11999,
                'stock': 25,
                'image_url': 'https://images.unsplash.com/photo-1527814050087-3793815479db?w=500',
                'is_featured': True
            },
            {
                'name': 'Razer DeathAdder V2 Gaming Mouse',
                'description': 'Ergonomic gaming mouse with 20,000 DPI optical sensor, 8 programmable buttons, Chroma RGB.',
                'category': gaming,
                'price': 9999,
                'original_price': 13999,
                'stock': 18,
                'image_url': 'https://images.unsplash.com/photo-1527814050087-3793815479db?w=500',
                'is_featured': False
            },
            {
                'name': 'Sony PlayStation 5 Console',
                'description': 'Next-gen gaming console with 825GB SSD, 4K gaming at 120fps, ray tracing, haptic feedback.',
                'category': gaming,
                'price': 74999,
                'original_price': 84999,
                'stock': 6,
                'image_url': 'https://images.unsplash.com/photo-1606144042614-b2417e99c4e3?w=500',
                'is_featured': True
            },
            {
                'name': 'Microsoft Xbox Series S',
                'description': 'Compact next-gen console with 512GB SSD, 1440p gaming, Game Pass compatible. Great value.',
                'category': gaming,
                'price': 42999,
                'original_price': 49999,
                'stock': 12,
                'image_url': 'https://images.unsplash.com/photo-1621259182978-fbf93132d53d?w=500',
                'is_featured': True
            },
            {
                'name': 'Nintendo Switch OLED Model',
                'description': '7-inch OLED screen, enhanced audio, 64GB storage. Play at home or on the go.',
                'category': gaming,
                'price': 45999,
                'original_price': 52999,
                'stock': 10,
                'image_url': 'https://images.unsplash.com/photo-1578303512597-81e6cc155b3e?w=500',
                'is_featured': False
            },
            {
                'name': 'Xbox Wireless Controller - Carbon Black',
                'description': 'Official Xbox controller with textured grip, Bluetooth connectivity, 40-hour battery life.',
                'category': gaming,
                'price': 7999,
                'original_price': 9999,
                'stock': 35,
                'image_url': 'https://images.unsplash.com/photo-1593305841991-05c297ba4575?w=500',
                'is_featured': False
            },
            {
                'name': 'PlayStation DualSense Controller - White',
                'description': 'Innovative PS5 controller with haptic feedback, adaptive triggers, built-in microphone.',
                'category': gaming,
                'price': 8999,
                'original_price': 10999,
                'stock': 28,
                'image_url': 'https://images.unsplash.com/photo-1592840496694-26d035b52b48?w=500',
                'is_featured': False
            },
            {
                'name': 'SteelSeries Arctis 5 Gaming Headset',
                'description': 'RGB gaming headset with DTS Headphone:X v2.0 surround sound, retractable mic.',
                'category': gaming,
                'price': 12999,
                'original_price': 16999,
                'stock': 15,
                'image_url': 'https://images.unsplash.com/photo-1618366712010-f4ae9c647dcb?w=500',
                'is_featured': False
            },

            # ELECTRONICS CATEGORY
            {
                'name': 'Apple Watch Series 9 GPS 45mm',
                'description': 'Advanced smartwatch with Always-On Retina display, heart rate monitor, ECG, and fitness tracking.',
                'category': electronics,
                'price': 52999,
                'original_price': 64999,
                'stock': 10,
                'image_url': 'https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=500',
                'is_featured': True
            },
            {
                'name': 'Samsung Galaxy Watch 6 Classic',
                'description': 'Premium smartwatch with rotating bezel, health sensors, GPS, and 5-day battery life.',
                'category': electronics,
                'price': 42999,
                'original_price': 54999,
                'stock': 15,
                'image_url': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500',
                'is_featured': True
            },
            {
                'name': 'Xiaomi Mi Band 8 Fitness Tracker',
                'description': 'Affordable fitness tracker with heart rate monitor, sleep tracking, and 14-day battery life.',
                'category': electronics,
                'price': 4999,
                'original_price': 6999,
                'stock': 50,
                'image_url': 'https://images.unsplash.com/photo-1575311373937-040b8e1fd5b6?w=500',
                'is_featured': False
            },
            {
                'name': 'Huawei Watch GT 3 Pro',
                'description': 'Premium smartwatch with titanium body, AMOLED display, and comprehensive health monitoring.',
                'category': electronics,
                'price': 38999,
                'original_price': 47999,
                'stock': 12,
                'image_url': 'https://images.unsplash.com/photo-1434494878577-86c23bcb06b9?w=500',
                'is_featured': False
            },
            {
                'name': 'Blue Yeti USB Microphone',
                'description': 'Professional USB mic for streaming, podcasting, and recording. Multiple pickup patterns.',
                'category': electronics,
                'price': 18999,
                'original_price': 24999,
                'stock': 15,
                'image_url': 'https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=500',
                'is_featured': True
            },
            {
                'name': 'HyperX QuadCast S RGB USB Microphone',
                'description': 'Stunning RGB USB mic with anti-vibration shock mount, tap-to-mute sensor, and gain control.',
                'category': electronics,
                'price': 22999,
                'original_price': 29999,
                'stock': 10,
                'image_url': 'https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=500',
                'is_featured': False
            },
            {
                'name': 'Rode NT-USB Mini USB Microphone',
                'description': 'Compact studio-quality USB mic perfect for streaming, gaming, and content creation.',
                'category': electronics,
                'price': 14999,
                'original_price': 19999,
                'stock': 18,
                'image_url': 'https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=500',
                'is_featured': False
            },

            # ACCESSORIES CATEGORY
            {
                'name': 'Anker PowerCore 20000mAh Power Bank',
                'description': 'High-capacity portable charger with dual USB ports, fast charging, and PowerIQ technology.',
                'category': accessories,
                'price': 4999,
                'original_price': 6999,
                'stock': 45,
                'image_url': 'https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=500',
                'is_featured': False
            },
            {
                'name': 'Oraimo 10000mAh Fast Charge Power Bank',
                'description': 'Compact power bank with 18W fast charging, dual USB output, and LED display.',
                'category': accessories,
                'price': 2499,
                'original_price': 3499,
                'stock': 60,
                'image_url': 'https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=500',
                'is_featured': False
            },
            {
                'name': 'Belkin 7-in-1 USB-C Hub',
                'description': 'Multiport hub with HDMI 4K, USB 3.0, SD/microSD readers, and 100W power delivery.',
                'category': accessories,
                'price': 6999,
                'original_price': 9999,
                'stock': 25,
                'image_url': 'https://images.unsplash.com/photo-1625948515291-69613efd103f?w=500',
                'is_featured': False
            },
            {
                'name': 'Spigen Rugged Armor Phone Case',
                'description': 'Durable phone case with carbon fiber texture, raised bezels for screen protection.',
                'category': accessories,
                'price': 1499,
                'original_price': 2499,
                'stock': 80,
                'image_url': 'https://images.unsplash.com/photo-1601593346740-925612772716?w=500',
                'is_featured': False
            },
        ]

        created_count = 0
        for product_data in products:
            product = Product.objects.create(**product_data)
            created_count += 1
            self.stdout.write(self.style.SUCCESS(f'Created: {product.name} - Ksh {product.price}'))

        self.stdout.write(self.style.SUCCESS(f'\n✅ Successfully created {created_count} Kenyan market products!'))
        self.stdout.write(self.style.SUCCESS(f'Categories: Audio, Computers, Gaming, Electronics, Accessories'))
