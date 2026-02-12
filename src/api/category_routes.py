from fastapi import APIRouter, HTTPException, status
from typing import List
from uuid import UUID
from ..services.category_service import CategoryService
from ..schemas.category_schema import CategoryCreate, CategoryResponse

router = APIRouter(prefix="/categories", tags=["Categories"])
service = CategoryService()


@router.post("", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate):
    return service.create_category(
        name=category.name,
        description=category.description
    )


@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: UUID):
    category = service.get_category(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.get("", response_model=List[CategoryResponse])
def get_categories(skip: int = 0, limit: int = 10):
    return service.get_all_categories(skip, limit)


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: UUID):
    deleted = service.delete_category(category_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Category not found")
