
class FakeModel(object):

    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            self.__dict__[k] = v