from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional

T = TypeVar("T")


class IRepository(ABC, Generic[T]):

    @abstractmethod
    def get_by_id(self, item_id) -> Optional[T]:
        pass

    @abstractmethod
    def get_all(self, skip: int = 0, limit: int = 10) -> List[T]:
        pass

    @abstractmethod
    def add(self, item: T) -> T:
        pass

    @abstractmethod
    def update(self, item: T) -> T:
        pass

    @abstractmethod
    def delete(self, item_id) -> bool:
        pass
