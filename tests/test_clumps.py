from unittest.case import TestCase

from bamboo_boy.materials import Clump
from bamboo_boy.utils import with_canopy, UnclumpableObject
from hypothetical_clumps import UndifferentiatedClump, UndifferentiatedClumpWithFactory, FakeFactory, ParentClump


class ClumpTests(TestCase):

    def test_clump_change_causes_canopy_in_function(self):
        '''
        Tests that a Clump causes a canopy to be available to a function.
        '''

        @with_canopy(UndifferentiatedClump)
        def clumped_function(canopy):
            # The thing changed when the state changed.
            self.assertEqual(canopy.thing, "This is a thing.")

        clumped_function()


    def test_factory_is_activated(self):

        number_to_create = 3

        @with_canopy(UndifferentiatedClumpWithFactory, number_to_create)
        def function_supplied_with_factory(canopy):
            factory_results = canopy.objects[FakeFactory]
            first_batch = factory_results[0]
            self.assertEqual(len(first_batch), 3)

        function_supplied_with_factory()


    def test_wrong_class_raises_error(self):

        def decorate_a_class_that_is_not_a_testcase():

            @with_canopy(Clump)
            class BadClass(object):
                pass

            wrong_object = BadClass()

        self.assertRaises(UnclumpableObject,
                          decorate_a_class_that_is_not_a_testcase,
                          )

    def test_function_that_takes_no_arguments_raises_error(self):

        @with_canopy(Clump)
        def func_that_takes_no_args():
            self.fail("This function is not eligible for a canopy - it doesn't take an argument.")

        self.assertRaises(UnclumpableObject,
                          func_that_takes_no_args,
                          )



class CanopyTests(TestCase):

    def test_access_subcanopies(self):

        @with_canopy(ParentClump)
        def clumped_function(canopy):
            self.assertEqual(canopy.subcanopies['ChildClump'].small_thing,
                             "This a a thing on a child clump.")

        clumped_function()
