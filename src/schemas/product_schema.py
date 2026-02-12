from pydantic import BaseModel, Field
from uuid import UUID
from decimal import Decimal
from typing import List, Optional


class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal = Field(..., gt=0)
    sku: str
    category_ids: Optional[List[UUID]] = None

class ProductUpdate(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal = Field(..., gt=0)
    sku: str
    category_ids: Optional[List[UUID]] = None


class ProductResponse(BaseModel):
    id: UUID
    name: str
    description: Optional[str]
    price: Decimal
    sku: str

    class Config:
        from_attributes = True
