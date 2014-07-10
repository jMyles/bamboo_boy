from bamboo_boy.states import State
from models import FakeModel

class FakeState(State):

    def build(self):
        self.thing = "This is a thing."


class FakeFactory(object):

    @classmethod
    def create_batch(cls, quantity):
        return [FakeModel(value=n) for n in range(quantity)]

class FakeStateWithFactory(State):

    def __init__(self, quantity, *args, **kwargs):
        self.quantity = quantity
        super(FakeStateWithFactory, self).__init__(*args, **kwargs)

    def build(self):
     self.include_factory(FakeFactory, self.quantity)