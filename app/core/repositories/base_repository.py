from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Sequence

T = TypeVar('T')


class BaseRepository(ABC, Generic[T]):

    @abstractmethod
    def insert(self, entity: T) -> T:
        raise NotImplementedError()

    @abstractmethod
    def update(self, entity: T) -> T | None:
        raise NotImplementedError()

    @abstractmethod
    def get_by_id(self, entity_id: int) -> T | None:
        raise NotImplementedError()

    @abstractmethod
    def get_all(self) -> Sequence[T]:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, entity_id: int):
        raise NotImplementedError()
