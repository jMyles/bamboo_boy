Bamboo Boy is a way to share setup and teardown logic between tests, deployments, and development environments.  It can reduce boilerplate logic in test methods, eliminate the need for fixtures or traditional scaffolding, and promote separation of logic between test state and assertions.

The "Boy" is a reference to utilizing factory_boy and extending its basic philosophy.

The "Bamboo" is the basis of the implementation metaphor:

* A "Clump" is a collection of objects and setup / teardown logic.
* A "canopy" is built by running the "build_canopy" method of a Clump.
* The canopy is used to access the objects.  A function is said to be running "with a canopy" if it uses the @with_canopy decorator.


# Quickstart

Suppose you have a model Thing and a factory ThingFactory.

```python
from bamboo_boy.materials import Clump

class ThingExists(Clump):
    '''
    Ensures that three Thing objects exist.
    '''
    def build_canopy(self):
        self.include_factory(ThingFactory, 3)  # We can also include *args and **kwargs here; they'll be passed on to the factory
```

Then, in a test:

```python
from bamboo_boy.utils import with_canopy

@with_canopy(ThingExists)
class ThingTests(TestCase):

    def test_that_thing_does_its_thing:
        things = self.canopy.objects[ThingFactory]
        first_thing = things[0]
        self.assertTrue(first_thing.do_your_thing())
```
