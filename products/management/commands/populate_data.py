from django.core.management.base import BaseCommand
from products.models import Category, Product


class Command(BaseCommand):
    help = 'Populate database with sample shoe store data'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create categories
        categories_data = [
            {'name': 'Sports Shoes', 'description': 'Athletic and sports footwear'},
            {'name': 'Casual Shoes', 'description': 'Everyday comfortable shoes'},
            {'name': 'Formal Shoes', 'description': 'Professional and dress shoes'},
            {'name': 'Sneakers', 'description': 'Trendy and fashionable sneakers'},
        ]
        
        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name']
            )
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(f'Created category: {category.name}')
        
        # Sample products data
        products_data = [
            {
                'name': 'Nike Air Max 270',
                'description': 'Experience the evolution of comfort with the Nike Air Max 270. It features Nike\'s largest heel Air unit yet for a soft ride that feels as impossible as it looks.',
                'price': 149.99,
                'category': 'Sports Shoes',
                'stock': 25
            },
            {
                'name': 'Adidas Ultraboost 22',
                'description': 'Push your running limits in these adidas Ultraboost 22 shoes. The responsive BOOST midsole combines with a stretchy knit upper for endless energy.',
                'price': 179.99,
                'category': 'Sports Shoes',
                'stock': 30
            },
            {
                'name': 'Converse Chuck Taylor All Star',
                'description': 'The Chuck Taylor All Star is the most iconic sneaker in the world, recognized for its unmistakable silhouette, star-centered ankle patch and cultural authenticity.',
                'price': 64.99,
                'category': 'Casual Shoes',
                'stock': 45
            },
            {
                'name': 'Vans Old Skool',
                'description': 'The Old Skool was our first footwear design to showcase the famous Vans Sidestripe—although back then it was just a simple doodle drawn by founder Paul Van Doren.',
                'price': 59.99,
                'category': 'Casual Shoes',
                'stock': 35
            },
            {
                'name': 'Cole Haan Grand Central Oxford',
                'description': 'This versatile oxford seamlessly bridges the gap between dress and casual, featuring premium leather construction and modern comfort technology.',
                'price': 249.99,
                'category': 'Formal Shoes',
                'stock': 20
            },
            {
                'name': 'Clarks Desert Boot',
                'description': 'An icon since 1950, the Desert Boot is a simple, timeless design. Made from premium suede with our signature crepe sole.',
                'price': 139.99,
                'category': 'Formal Shoes',
                'stock': 18
            },
            {
                'name': 'Jordan 1 Retro High',
                'description': 'The Air Jordan 1 Retro High OG brings back the classic basketball shoe that started it all with its iconic design and premium materials.',
                'price': 169.99,
                'category': 'Sneakers',
                'stock': 15
            },
            {
                'name': 'New Balance 990v5',
                'description': 'The 990v5 is the most refined version of the 990 series, featuring superior materials and craftsmanship that made in USA represents.',
                'price': 184.99,
                'category': 'Sneakers',
                'stock': 22
            },
            {
                'name': 'Puma RS-X3',
                'description': 'The RS-X3 takes the retro-futuristic design of the original RS series and brings it into the modern era with updated materials and bold colorways.',
                'price': 89.99,
                'category': 'Sneakers',
                'stock': 28
            },
            {
                'name': 'Timberland 6-Inch Premium Boot',
                'description': 'Our original waterproof boot is built to last. Premium nubuck leather, seam-sealed construction and our exclusive anti-fatigue technology.',
                'price': 189.99,
                'category': 'Casual Shoes',
                'stock': 16
            }
        ]
        
        # Create products
        for product_data in products_data:
            category = categories[product_data['category']]
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults={
                    'description': product_data['description'],
                    'price': product_data['price'],
                    'category': category,
                    'stock': product_data['stock']
                }
            )
            if created:
                self.stdout.write(f'Created product: {product.name}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with sample data!')
        )
