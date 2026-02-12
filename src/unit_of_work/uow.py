from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..repositories.product_repository import ProductRepository
from ..repositories.category_repository import CategoryRepository


class IUnitOfWork:
    def __enter__(self):
        raise NotImplementedError

    def __exit__(self, *args):
        raise NotImplementedError

    def commit(self):
        raise NotImplementedError

    def rollback(self):
        raise NotImplementedError


class SQLUnitOfWork(IUnitOfWork):

    def __init__(self):
        self.session: Session | None = None
        self.products = None
        self.categories = None

    def __enter__(self):
        self.session = SessionLocal()
        self.products = ProductRepository(self.session)
        self.categories = CategoryRepository(self.session)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.rollback()
        else:
            self.commit()
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
