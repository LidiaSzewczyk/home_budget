from abc import ABC, abstractmethod


class AbsAmount(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def uuid(self):
        pass

    @property
    @abstractmethod
    def created(self):
        pass

    @property
    @abstractmethod
    def category(self):
        pass

    @abstractmethod
    def amount(self):
        pass