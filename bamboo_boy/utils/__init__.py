
class UnclumpableObject(TypeError):
    pass

def with_canopy(clump_class, *clump_args, **clump_kwargs):
    '''
    Can decorate a function or class.
    The function or class will live under a canopy built by running build_canopy from a Clump.

    A decorated class is given a "canopy" attribute allowing access to the clump material.

    A function receives - and must allow - the canopy as its first argument.

    (Thus, we raise TypeError if a function doesn't take any positional arguments.
    If the function does take a positional argument and the author forgets that it will
    be a canopy, unpredictable results may ensue.)
    '''
    def closure(obj):
        '''
        A closure containing the function that applies the clump to the decorated object in scope.
        '''
        def clump_run(*args, **kwargs):
            '''
            Runs the clump, returning the object.

            For TestCases, also runs setUp() and tearDown()
            '''
            clump = clump_class(*clump_args, obj=obj, **clump_kwargs)
            if hasattr(obj, 'setUp'):  # IE, a TestCase
                old_setUp = obj.setUp

                def new_setup(*args, **kwargs):
                    clump.build_canopy()
                    clump.deliver_canopy()
                    old_setUp(*args, **kwargs)

                old_tearDown = obj.tearDown

                def new_teardown(*args, **kwargs):
                    clump.retract_canopy()
                    clump.destroy_canopy()
                    old_tearDown(*args, **kwargs)

                obj.setUp = new_setup
                obj.tearDown = new_teardown

                obj.canopy = clump

                return obj

            else:
                def new_func():
                    clump.build_canopy()
                    clump.deliver_canopy()
                    try:
                        obj(clump, *args, **kwargs)
                    except TypeError, e:
                        raise UnclumpableObject("Please pass a TestCase or a function that takes canopy as its first argument.  This decorator is not appropriate for other objects.")
                    clump.retract_canopy()
                    clump.destroy_canopy()
                return new_func
        canopy = clump_run()
        return canopy
    return closure


