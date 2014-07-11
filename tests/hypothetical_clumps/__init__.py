from bamboo_boy.materials import Clump
from models import FakeModel

class UndifferentiatedClump(Clump):

    def build(self):
        self.thing = "This is a thing."


class FakeFactory(object):

    @classmethod
    def create_batch(cls, quantity):
        return [FakeModel(value=n) for n in range(quantity)]

class UndifferentiatedClumpWithFactory(Clump):

    def __init__(self, quantity, *args, **kwargs):
        self.quantity = quantity
        super(UndifferentiatedClumpWithFactory, self).__init__(*args, **kwargs)

    def build(self):
     self.include_factory(FakeFactory, self.quantity)


class ChildClump(Clump):
    def build(self):
        self.small_thing = "This a a thing on a child clump."


class ParentClump(Clump):
    constituent_clumps = [ChildClump]