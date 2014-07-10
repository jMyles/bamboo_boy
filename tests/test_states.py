from unittest.case import TestCase

from bamboo_boy.states import State
from bamboo_boy.utils import require_state, WrongObjectForState
from fake_states import FakeState, FakeStateWithFactory, FakeFactory


class StateTests(TestCase):

    def test_state_change_causes_test_bed(self):
        '''
        Tests that a State causes test_bed to be available.
        '''

        @require_state(FakeState)
        def now_the_state_is_for_real(test_bed):
            # The thing changed when the state changed.
            self.assertEqual(test_bed.thing, "This is a thing.")

        now_the_state_is_for_real()


    def test_factory_is_activated(self):

        number_to_create = 3

        @require_state(FakeStateWithFactory, number_to_create)
        def function_supplied_with_factory(test_bed):
            factory_results = test_bed.objects[FakeFactory]
            first_batch = factory_results[0]
            self.assertEqual(len(first_batch), 3)

        function_supplied_with_factory()


    def test_wrong_object_raises_error(self):

        def bad_decorated():
            @require_state(State)

            class BadClass(object):
                pass

            wrong_object = BadClass()

        self.assertRaises(WrongObjectForState,
                          bad_decorated,
                          )