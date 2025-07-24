
from abc import ABC, abstractmethod


class MDComponent(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def ToString(self):
        pass