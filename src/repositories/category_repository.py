from sqlalchemy.orm import Session
from typing import List, Optional
from .base import IRepository
from ..models.category import Category


class CategoryRepository(IRepository[Category]):

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, item_id) -> Optional[Category]:
        return self.session.query(Category).filter(Category.id == item_id).first()

    def get_all(self, skip: int = 0, limit: int = 10) -> List[Category]:
        return self.session.query(Category).offset(skip).limit(limit).all()

    def add(self, item: Category) -> Category:
        self.session.add(item)
        return item

    def update(self, item: Category) -> Category:
        return item

    def delete(self, item_id) -> bool:
        category = self.get_by_id(item_id)
        if not category:
            return False
        self.session.delete(category)
        return True
