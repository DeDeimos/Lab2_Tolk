from abc import ABC
from abc import abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
