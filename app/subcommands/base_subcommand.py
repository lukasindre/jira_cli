from abc import ABC, abstractmethod


class BaseSubcommand(ABC):
    @abstractmethod
    def command(self):
        """Abstract method named command.

        This is here to ensure that any future subcommands inheriting
        from this class implement the command method, as that is how
        the subcommands are loaded into the command group.
        """
        pass
