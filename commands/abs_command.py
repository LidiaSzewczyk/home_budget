from abc import ABC, abstractmethod

# from uuid.uuid import UUID


class AbsCommand(ABC):
    # dashboard = []
    #
    # uuid = UUID()

    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def execute(self):
        pass
