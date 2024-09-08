from abc import ABC, abstractmethod

class AbstractUnitOfWork(ABC):

    @abstractmethod
    def begin_transaction(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def commit_transaction(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def rollback_transaction(self) -> None:
        raise NotImplementedError()