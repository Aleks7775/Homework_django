from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category, _ = Category.objects.get_or_create(name='Овощи')

        products = [
            {'name': 'Картошка',
             'image': '', 'price': 100, 'category': category},
            {'name': 'Помидоры',
             'price': 200, 'category': category}
        ]
        for product_in_data in products:
            product, created = Product.objects.get_or_create(**product_in_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added book: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Book already exists: {product.name}'))
