from sqlalchemy.orm import Session

from .unit_of_work import AbstractUnitOfWork


class UnitOfWorkImpl(AbstractUnitOfWork):

    def __init__(self, session: Session):
        self._session = session

    def begin_transaction(self) -> None:
        self._session.begin()

    def commit_transaction(self) -> None:
        self._session.commit()

    def rollback_transaction(self) -> None:
        self._session.rollback()