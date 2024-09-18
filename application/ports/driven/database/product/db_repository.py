from abc import ABC, abstractmethod


class ProductDBRepositoryPort(ABC):
    @abstractmethod
    def save(self, mail: str):
        pass
