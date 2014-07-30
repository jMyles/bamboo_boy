
Bamboo Boy is a way to share setup and teardown logic between tests,
deployments, and development environments. It can reduce boilerplate
logic in test methods, eliminate the need for fixtures or traditional
scaffolding, and promote separation of logic between test state and
assertions.

The "Boy" is a reference to utilizing factory\_boy and extending its
basic philosophy.

The "Bamboo" is the basis of the implementation metaphor:

-  A "Clump" is a collection of objects and setup / teardown logic.
-  A "canopy" is built by running the "build\_canopy" method of a Clump.
-  The canopy is used to access the objects. A function is said to be
   running "with a canopy" if it uses the @with\_canopy decorator.

Quickstart
----------

Maybe you already have the following Thing and its Factory.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    import factory
    
    
    class Thing(object):
        def do_your_thing(self):
            return True
    
        
    class ThingFactory(factory.Factory):
        class Meta:
            model = Thing
Now, you can create a "Clump" of reusable logic.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from bamboo_boy.materials import Clump
    
    
    class ThingExists(Clump):
        '''
        Ensures that three Thing objects exist.
        '''
        def build_canopy(self):
            self.include_factory(ThingFactory, 3)  # We can also include *args and **kwargs here; they'll be passed on to the factory
Then, in a test:
~~~~~~~~~~~~~~~~

.. code:: python

    import unittest
    from bamboo_boy.utils import with_canopy
    
    
    @with_canopy(ThingExists)
    class TestThings(unittest.TestCase):
    
        def test_that_thing_does_its_thing(self):
            lists_of_things = self.canopy.objects[ThingFactory]
            first_list_of_things = lists_of_things[0]
            first_thing = first_list_of_things[0]
            self.assertTrue(first_thing.do_your_thing())
Slightly more advanced
----------------------

Passing arguments thourgh with\_canopy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Suppose you need to be able to set the number of factory objects to
create not in the definition of the build\_canopy() method on the Clump,
but in the with\_canopy decorator.

.. code:: python

    class ExcitingThingsExist(Clump):
        '''
        Let the user specify how many things to create.
        '''
        def __init__(self, number_of_things):
            self.number_of_things = number_of_things
            super(ExcitingThingsExist, self).__init__()
        
        def build_canopy(self):
            self.include_factory(ThingFactory, self.number_of_things)
.. code:: python

    @with_canopy(ExcitingThingsExist, 4)
    class TestThings(unittest.TestCase):
        
        def test_that_there_are_four_things(self):
            number_of_things = self.canopy.objects[ThingFactory][0]
            self.assertEqual(len(number_of_things), 4)