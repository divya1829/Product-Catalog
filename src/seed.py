from decimal import Decimal
from .unit_of_work.uow import SQLUnitOfWork
from .models.product import Product
from .models.category import Category


def seed_database():

    with SQLUnitOfWork() as uow:

        # Check if already seeded
        existing_products = uow.products.get_all()
        if existing_products:
            print("Database already seeded. Skipping...")
            return

        print("Seeding database...")

        # Create Categories
        electronics = Category(name="Electronics", description="Electronic devices")
        clothing = Category(name="Clothing", description="Apparel and fashion")
        books = Category(name="Books", description="Books and literature")

        uow.categories.add(electronics)
        uow.categories.add(clothing)
        uow.categories.add(books)

        # Create Products
        products = [
            Product(name="Laptop", description="Gaming laptop", price=Decimal("1200"), sku="SKU1", categories=[electronics]),
            Product(name="Smartphone", description="Latest smartphone", price=Decimal("800"), sku="SKU2", categories=[electronics]),
            Product(name="Headphones", description="Noise cancelling", price=Decimal("200"), sku="SKU3", categories=[electronics]),
            Product(name="T-Shirt", description="Cotton t-shirt", price=Decimal("25"), sku="SKU4", categories=[clothing]),
            Product(name="Jeans", description="Blue denim jeans", price=Decimal("50"), sku="SKU5", categories=[clothing]),
            Product(name="Jacket", description="Winter jacket", price=Decimal("120"), sku="SKU6", categories=[clothing]),
            Product(name="Novel", description="Fiction novel", price=Decimal("15"), sku="SKU7", categories=[books]),
            Product(name="Textbook", description="Science textbook", price=Decimal("60"), sku="SKU8", categories=[books]),
            Product(name="Notebook", description="Writing notebook", price=Decimal("5"), sku="SKU9", categories=[books]),
            Product(name="Tablet", description="Android tablet", price=Decimal("400"), sku="SKU10", categories=[electronics]),
        ]

        for product in products:
            uow.products.add(product)

        print("Seeding complete.")
