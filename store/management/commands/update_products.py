from django.core.management.base import BaseCommand
from store.models import Category, Product

class Command(BaseCommand):
    help = 'Update products with categories and images'

    def handle(self, *args, **kwargs):
        # Create categories
        categories_data = [
            {'name': 'Electronics', 'icon': '📱', 'description': 'Phones, Laptops, and Gadgets'},
            {'name': 'Audio', 'icon': '🎧', 'description': 'Headphones and Speakers'},
            {'name': 'Accessories', 'icon': '🔌', 'description': 'Phone and Computer Accessories'},
            {'name': 'Computers', 'icon': '💻', 'description': 'Laptops and Computer Equipment'},
            {'name': 'Gaming', 'icon': '🎮', 'description': 'Gaming Accessories'},
        ]

        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'icon': cat_data['icon'], 'description': cat_data['description']}
            )
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {category.name}'))

        # Update existing products with categories and images
        products_update = [
            {
                'name': 'Wireless Headphones',
                'category': categories['Audio'],
                'image_url': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500',
                'original_price': 249.99,
                'is_featured': True
            },
            {
                'name': 'Smart Watch',
                'category': categories['Electronics'],
                'image_url': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500',
                'original_price': 349.99,
                'is_featured': True
            },
            {
                'name': 'Laptop Stand',
                'category': categories['Accessories'],
                'image_url': 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500',
                'original_price': 69.99,
                'is_featured': False
            },
            {
                'name': 'Mechanical Keyboard',
                'category': categories['Gaming'],
                'image_url': 'https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=500',
                'original_price': 159.99,
                'is_featured': True
            },
            {
                'name': 'Wireless Mouse',
                'category': categories['Accessories'],
                'image_url': 'https://images.unsplash.com/photo-1527814050087-3793815479db?w=500',
                'original_price': 49.99,
                'is_featured': False
            },
            {
                'name': 'USB-C Hub',
                'category': categories['Accessories'],
                'image_url': 'https://images.unsplash.com/photo-1625948515291-69613efd103f?w=500',
                'original_price': 79.99,
                'is_featured': False
            },
            {
                'name': 'Portable Charger',
                'category': categories['Accessories'],
                'image_url': 'https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=500',
                'original_price': 59.99,
                'is_featured': False
            },
            {
                'name': 'Webcam HD',
                'category': categories['Computers'],
                'image_url': 'https://images.unsplash.com/photo-1593642702749-b7d2a804fbcf?w=500',
                'original_price': 99.99,
                'is_featured': False
            },
            {
                'name': 'Phone Case',
                'category': categories['Accessories'],
                'image_url': 'https://images.unsplash.com/photo-1601593346740-925612772716?w=500',
                'original_price': 29.99,
                'is_featured': False
            },
            {
                'name': 'Bluetooth Speaker',
                'category': categories['Audio'],
                'image_url': 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=500',
                'original_price': 119.99,
                'is_featured': True
            },
        ]

        for product_data in products_update:
            try:
                product = Product.objects.get(name=product_data['name'])
                product.category = product_data['category']
                product.image_url = product_data['image_url']
                product.original_price = product_data['original_price']
                product.is_featured = product_data['is_featured']
                product.save()
                self.stdout.write(self.style.SUCCESS(f'Updated product: {product.name}'))
            except Product.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Product not found: {product_data["name"]}'))

        self.stdout.write(self.style.SUCCESS('\nProducts updated successfully!'))
