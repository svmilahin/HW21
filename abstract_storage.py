from abc import ABC, abstractmethod


class AbstractStorage(ABC):

    def __init__(self):
        self._items = {}
        self._capacity = 0

    @abstractmethod
    def add(self, title: str, qty: int) -> None:
        pass

    @abstractmethod
    def remove(self, title: str, qty: int) -> None:
        pass

    @property
    @abstractmethod
    def get_items(self) -> dict[str, int]:
        pass

    @abstractmethod
    def get_free_space(self) -> int:
        pass

    @abstractmethod
    def get_unique_items_count(self) -> int:
        pass
