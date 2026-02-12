from fastapi import APIRouter, HTTPException, status
from typing import List
from uuid import UUID
from ..services.product_service import ProductService
from ..schemas.product_schema import ProductCreate, ProductResponse
from ..schemas.product_schema import ProductCreate, ProductResponse, ProductUpdate
from decimal import Decimal

router = APIRouter(prefix="/products", tags=["Products"])
service = ProductService()


@router.post("", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate):
    try:
        created = service.create_product(
            name=product.name,
            description=product.description,
            price=product.price,
            sku=product.sku,
            category_ids=product.category_ids
        )
        return created
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/search", response_model=List[ProductResponse])
def search_products(
    q: str = None,
    category_id: UUID = None,
    min_price: Decimal = None,
    max_price: Decimal = None,
    skip: int = 0,
    limit: int = 10
):
    return service.search_products(
        q=q,
        category_id=category_id,
        min_price=min_price,
        max_price=max_price,
        skip=skip,
        limit=limit
    )


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: UUID):
    product = service.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.get("", response_model=List[ProductResponse])
def get_products(skip: int = 0, limit: int = 10):
    return service.get_all_products(skip, limit)


@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: UUID, product: ProductUpdate):
    try:
        updated = service.update_product(
            product_id=product_id,
            name=product.name,
            description=product.description,
            price=product.price,
            sku=product.sku,
            category_ids=product.category_ids
        )

        if not updated:
            raise HTTPException(status_code=404, detail="Product not found")

        return updated

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: UUID):
    deleted = service.delete_product(product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
