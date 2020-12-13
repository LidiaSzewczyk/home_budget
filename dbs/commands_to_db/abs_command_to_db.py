from abc import ABC, abstractmethod

from dbs.DbConnection import DbConnection


class AbsDb(ABC):

    def __init__(self):
        self.db = DbConnection().db
        self.cursor = self.db.cursor()

    @abstractmethod
    def do(self, *args):
        pass
