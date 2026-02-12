from uuid import UUID
from decimal import Decimal
from typing import List, Optional
from ..models.product import Product
from ..unit_of_work.uow import SQLUnitOfWork


class ProductService:

    def create_product(
        self,
        name: str,
        description: str,
        price: Decimal,
        sku: str,
        category_ids: Optional[List[UUID]] = None
    ) -> Product:

        with SQLUnitOfWork() as uow:

            product = Product(
                name=name,
                description=description,
                price=price,
                sku=sku
            )

            if category_ids:
                categories = []
                for cat_id in category_ids:
                    category = uow.categories.get_by_id(cat_id)
                    if not category:
                        raise ValueError(f"Category {cat_id} not found")
                    categories.append(category)

                product.categories = categories

            uow.products.add(product)

            return product

    def get_product(self, product_id: UUID) -> Optional[Product]:
        with SQLUnitOfWork() as uow:
            return uow.products.get_by_id(product_id)

    def get_all_products(self, skip: int = 0, limit: int = 10):
        with SQLUnitOfWork() as uow:
            return uow.products.get_all(skip, limit)

    def delete_product(self, product_id: UUID) -> bool:
        with SQLUnitOfWork() as uow:
            return uow.products.delete(product_id)

    def update_product(
        self,
        product_id: UUID,
        name: str,
        description: str,
        price: Decimal,
        sku: str,
        category_ids: Optional[List[UUID]] = None
    ):

        with SQLUnitOfWork() as uow:

            product = uow.products.get_by_id(product_id)
            if not product:
                return None

            product.name = name
            product.description = description
            product.price = price
            product.sku = sku

            if category_ids is not None:
                categories = []
                for cat_id in category_ids:
                    category = uow.categories.get_by_id(cat_id)
                    if not category:
                        raise ValueError(f"Category {cat_id} not found")
                    categories.append(category)

                product.categories = categories

            return product
    def search_products(
        self,
        q: str = None,
        category_id=None,
        min_price=None,
        max_price=None,
        skip: int = 0,
        limit: int = 10
    ):
        with SQLUnitOfWork() as uow:
            return uow.products.search(
                q=q,
                category_id=category_id,
                min_price=min_price,
                max_price=max_price,
                skip=skip,
                limit=limit
            )
