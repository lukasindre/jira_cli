from abc import ABC, abstractmethod


class BaseSubcommand(ABC):
    @abstractmethod
    def command(self):
        pass
