
class WrongObjectForState(TypeError):
    pass

def require_state(state_class, *state_args, **state_kwargs):
    '''
    Can decorate a function or class.

    For <class>, builds state_class and adds it as <class>.test_bed.

    For a function, builds state_class and adds it as first argument.

    (Thus, obviously raises TypeError if function doesn't take any positional arguments.
    If the function does take a positional argument and the author forgets that it will
    be a state_class, unpredictable results may ensue.)
    '''
    def closure(obj):
        '''
        A closure containing the state function with the decorated object in scope.
        '''
        def state_run(*args, **kwargs):
            '''
            Runs the state, returning the object.

            For TestCases, also runs setUp() and tearDown()
            '''
            state = state_class(*state_args, **state_kwargs)
            if hasattr(obj, 'setUp'):  # IE, a TestCase
                old_setUp = obj.setUp
                def new_setup(*args, **kwargs):
                    state.build()
                    old_setUp(*args, **kwargs)


                old_tearDown = obj.tearDown
                def new_teardown(*args, **kwargs):
                    state.destroy()
                    old_tearDown(*args, **kwargs)

                obj.setUp = new_setup
                obj.tearDown = new_teardown

                obj.test_bed = state

                return obj

            else:
                def new_func():
                    test_bed = state.build()
                    try:
                        obj(state, *args, **kwargs)
                    except TypeError, e:
                        raise WrongObjectForState("Please pass a TestCase or a function that takes test_bed as its first argument.  This decorator is not appropriate for other objects.")
                    state.destroy()
                return new_func
        return state_run()
    return closure


