class State(object):

    child_states = {}

    def __init__(self):
        self.factory_configs = []
        self.objects = {}
        self.inherited_states = {}

    def inherit_state(self, state_class):
        '''
        Takes 1 or more children of State.
        Builds each, adding their objects to a dict.  Returns that dict.
        '''
        state = state_class()
        state.build()
        self.inherited_states[state_class.__name__] = state


    def include_factory(self, factory, quantity, **kwargs):
        '''
        Add the result of a Factory.create_batch to this State's objects dict.
        '''
        factory_result = factory.create_batch(quantity, **kwargs)
        try:
            self.objects.setdefault(factory, []).append(factory_result)
        except AttributeError, e:
            message = "%s -- Did you forget to run the __init__ of the parent State?" % e.message
            raise AttributeError(message)
        return factory_result


    def build(self):
        for child_state in self.child_states:
            self.inherit_state(child_state)

    def destroy(self):
        pass