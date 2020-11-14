from datetime import datetime

from amount.abs_amount import AbsAmount



class Expense(AbsAmount):

    def __init__(self, name, category, amount, uuid):
        self._uuid = next(uuid)
        self._amount = amount
        self._category = category
        self._name = name
        self._created = datetime.now()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_val):
        self._name = new_val

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, new_val):
        self._amount = new_val

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_val):
        self._category = new_val

    @property
    def uuid(self):
        return self._uuid

    @property
    def created(self):
        return self._created

    @created.setter
    def created(self, new_val):
        self._created = new_val

    def __repr__(self):
        return f'class Expense (id: {self.uuid}, category:{self.category}, name:{self.name}, amount: {self.amount}, created: {self.created})'
