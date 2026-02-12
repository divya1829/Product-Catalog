from uuid import UUID
from typing import Optional
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from ..models.category import Category
from ..unit_of_work.uow import SQLUnitOfWork


class CategoryService:

    def create_category(self, name: str, description: str) -> Category:
        try:
            with SQLUnitOfWork() as uow:
                category = Category(name=name, description=description)
                uow.categories.add(category)
                return category
        except IntegrityError:
            raise HTTPException(
                status_code=400,
                detail="Category with this name already exists"
            )

    def get_category(self, category_id: UUID) -> Optional[Category]:
        with SQLUnitOfWork() as uow:
            return uow.categories.get_by_id(category_id)

    def get_all_categories(self, skip: int = 0, limit: int = 10):
        with SQLUnitOfWork() as uow:
            return uow.categories.get_all(skip, limit)

    def delete_category(self, category_id: UUID) -> bool:
        with SQLUnitOfWork() as uow:
            return uow.categories.delete(category_id)
