from sqlalchemy.orm import Session
from typing import List, Optional
from .base import IRepository
from ..models.product import Product
from sqlalchemy import or_

class ProductRepository(IRepository[Product]):

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, item_id) -> Optional[Product]:
        return self.session.query(Product).filter(Product.id == item_id).first()

    def get_all(self, skip: int = 0, limit: int = 10) -> List[Product]:
        return self.session.query(Product).offset(skip).limit(limit).all()

    def add(self, item: Product) -> Product:
        self.session.add(item)
        return item

    def update(self, item: Product) -> Product:
        return item

    def delete(self, item_id) -> bool:
        product = self.get_by_id(item_id)
        if not product:
            return False
        self.session.delete(product)
        return True


    def search(
        self,
        q: str = None,
        category_id=None,
        min_price=None,
        max_price=None,
        skip: int = 0,
        limit: int = 10
    ):
        query = self.session.query(Product)

        if q:
            query = query.filter(
                or_(
                    Product.name.ilike(f"%{q}%"),
                    Product.description.ilike(f"%{q}%")
                )
            )

        if category_id:
            query = query.join(Product.categories).filter(
                Product.categories.any(id=category_id)
            )

        if min_price is not None:
            query = query.filter(Product.price >= min_price)

        if max_price is not None:
            query = query.filter(Product.price <= max_price)

        return query.offset(skip).limit(limit).all()
