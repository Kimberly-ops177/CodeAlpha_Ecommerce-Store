from django.core.management.base import BaseCommand
from store.models import Product

class Command(BaseCommand):
    help = 'Update products with realistic Kenyan market prices (researched Jan 2026)'

    def handle(self, *args, **kwargs):
        price_updates = {
            # AUDIO - Based on Jumia, Phone Place Kenya, Avechi research
            'Oraimo FreePods 3 TWS Earbuds': {'price': 4999, 'original_price': 6500},
            'Oraimo AirBuds 2 Wireless Earphones': {'price': 2499, 'original_price': 3500},
            'Samsung Galaxy Buds 2 Pro': {'price': 14999, 'original_price': 19999},
            'Apple AirPods Pro (2nd Gen)': {'price': 29999, 'original_price': 39999},
            'Apple AirPods (3rd Generation)': {'price': 19999, 'original_price': 25999},
            'Samsung Galaxy Buds FE': {'price': 9999, 'original_price': 14999},

            # COMPUTERS - Based on market research
            'HP EliteBook 840 G8 - Intel i5 11th Gen': {'price': 85000, 'original_price': 110000},
            'Dell Inspiron 15 3000 - AMD Ryzen 5': {'price': 55000, 'original_price': 72000},
            'Lenovo ThinkPad T14 Gen 3 - Intel i7': {'price': 125000, 'original_price': 165000},
            'Dell OptiPlex 7090 Desktop Mini PC': {'price': 65000, 'original_price': 85000},
            'HP Desktop Tower - Intel i3': {'price': 42000, 'original_price': 55000},
            'LG 24" Full HD IPS Monitor': {'price': 17999, 'original_price': 24999},
            'Dell 27" QHD Monitor - P2722H': {'price': 38999, 'original_price': 52999},
            'Logitech C920 HD Pro Webcam': {'price': 11999, 'original_price': 15999},
            'Original HP Laptop Battery - 4 Cell': {'price': 5500, 'original_price': 7500},
            'Dell 65W USB-C Laptop Charger': {'price': 3999, 'original_price': 5500},
            'HP 90W Smart AC Adapter': {'price': 3499, 'original_price': 4999},
            'Dell WD19 180W Docking Station': {'price': 28999, 'original_price': 38999},
            'Lenovo ThinkPad USB-C Dock Gen 2': {'price': 32999, 'original_price': 42999},

            # GAMING - Based on Jumia and gaming retailers
            'Logitech G502 HERO Gaming Mouse': {'price': 9999, 'original_price': 13999},
            'Razer DeathAdder V2 Gaming Mouse': {'price': 11999, 'original_price': 15999},
            'Sony PlayStation 5 Console': {'price': 119999, 'original_price': 139999},
            'Microsoft Xbox Series S': {'price': 54999, 'original_price': 64999},
            'Nintendo Switch OLED Model': {'price': 52999, 'original_price': 62999},
            'Xbox Wireless Controller - Carbon Black': {'price': 8999, 'original_price': 11999},
            'PlayStation DualSense Controller - White': {'price': 9999, 'original_price': 12999},
            'SteelSeries Arctis 5 Gaming Headset': {'price': 14999, 'original_price': 19999},

            # ELECTRONICS - Based on Phone Place Kenya, Gadgets Leo research
            'Apple Watch Series 9 GPS 45mm': {'price': 45999, 'original_price': 59999},
            'Samsung Galaxy Watch 6 Classic': {'price': 24999, 'original_price': 34999},
            'Xiaomi Mi Band 8 Fitness Tracker': {'price': 4999, 'original_price': 6999},
            'Huawei Watch GT 3 Pro': {'price': 32999, 'original_price': 42999},
            'Blue Yeti USB Microphone': {'price': 21999, 'original_price': 28999},
            'HyperX QuadCast S RGB USB Microphone': {'price': 25999, 'original_price': 32999},
            'Rode NT-USB Mini USB Microphone': {'price': 17999, 'original_price': 23999},

            # ACCESSORIES
            'Anker PowerCore 20000mAh Power Bank': {'price': 5999, 'original_price': 7999},
            'Oraimo 10000mAh Fast Charge Power Bank': {'price': 2999, 'original_price': 4299},
            'Belkin 7-in-1 USB-C Hub': {'price': 7999, 'original_price': 10999},
            'Spigen Rugged Armor Phone Case': {'price': 1999, 'original_price': 2999},
        }

        updated = 0
        for product_name, prices in price_updates.items():
            try:
                product = Product.objects.get(name=product_name)
                product.price = prices['price']
                product.original_price = prices['original_price']
                product.save()
                self.stdout.write(self.style.SUCCESS(
                    f'Updated: {product.name} - Ksh {product.price} (was Ksh {prices["original_price"]})'
                ))
                updated += 1
            except Product.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Product not found: {product_name}'))

        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully updated {updated} products with realistic Kenyan market prices!'))
        self.stdout.write(self.style.SUCCESS('Prices researched from: Jumia, Phone Place Kenya, Avechi, Gadgets Leo, Price in Kenya'))
