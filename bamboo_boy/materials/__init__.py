class Clump(object):

    constituent_clumps = {}

    def __init__(self):
        self.factory_configs = []
        self.objects = {}
        self.subcanopies = {}

    def consume_clump(self, clump_class):
        '''
        Takes 1 or more children of Clump.
        Builds each, adding their objects as values to a dict, with the class name as a value.
        Adds the dict as self.constituent_clumps.
        '''
        clump = clump_class()
        clump.build()
        self.subcanopies[clump_class.__name__] = clump

    def include_factory(self, factory, quantity, **kwargs):
        '''
        Add the result of a Factory.create_batch to this Clump's objects dict.
        '''
        factory_result = factory.create_batch(quantity, **kwargs)
        try:
            self.objects.setdefault(factory, []).append(factory_result)
        except AttributeError, e:
            message = "%s -- Did you forget to run the __init__ of the parent Clump?" % e.message
            raise AttributeError(message)
        return factory_result


    def build(self):
        for child_clump in self.constituent_clumps:
            self.consume_clump(child_clump)

    def destroy(self):
        pass