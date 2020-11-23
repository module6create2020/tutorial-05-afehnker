import pytest
from exercises.mate import Mate
from exercises.tutorial05 import update_element,update_element_left
import random


# No need to change these tests.
class TestExercise2_3_1_1:

    def test_repr(self):
        try:
            a = Mate("Kim", 42)
            result = str(a)
            if result != '(Kim, 42)':
                pytest.fail("Method '__repr__' failed to return '(Kim, 42)',"
                            "\n instead returned {}".format(result))
        except:
            pytest.fail("The method '__repr__' does not quite work yet")
        return None


class TestExercise2_3_2_1:

    def test_lt(self):
        try:
            for i in range(10):
                a_value = random.randrange(-3, 3)
                b_value = random.randrange(-3, 3)
                expected = a_value < b_value
                a = Mate("Kim", a_value)
                b = Mate("Fin", b_value)
                result = a < b
                if result != expected:
                    pytest.fail("Method '__lt__' failed  for '(Kim, {}) < (Fin, {})'."
                                "\n Returned {}. Expected {}.".format(a_value, b_value, result, expected))
                    return None
        except:
            pytest.fail(
                "The method '__lt__' does not quite work yet.")
        return None

class TestExercise2_3_2_3:

    def test_insert(self):
        alice = Mate("Alice", 14)
        bob = Mate("Bob", 14)
        carol = Mate("Carol", 13)
        dave = Mate("Dave", 14)
        eve = Mate("Eve", 15)
        a_list = [alice, bob, carol, dave, eve]
        a_list.sort()
        bob.value=15
        update_element(a_list, bob)
        assert a_list == [carol, alice, dave, eve, bob], \
            "The list should be [(Carol, 13), (Alice, 14), (Dave, 14), (Eve, 15), (Bob, 15)] "
        bob.value = 14
        update_element(a_list, bob)
        assert a_list == [carol, alice, dave, bob, eve], \
            "The list should be [(Carol, 13), (Alice, 14), (Dave, 14), (Bob, 14), (Eve, 15)] "
        bob.value = 13
        update_element(a_list, bob)
        assert a_list == [carol, bob, alice, dave, eve], \
            "The list should be [(Carol, 13), (Bob, 13), (Alice, 14), (Dave, 14), (Eve, 15)] "
        frank=Mate("Frank","35")
        update_element(a_list, frank)
        assert a_list == [carol, bob, alice, dave, eve], \
            "The list should be [(Carol, 13), (Bob, 13), (Alice, 14), (Dave, 14), (Eve, 15)] "



    def test_insert_left(self):
        alice = Mate("Alice", 14)
        bob = Mate("Bob", 14)
        carol = Mate("Carol", 13)
        dave = Mate("Dave", 14)
        eve = Mate("Eve", 15)
        a_list = [alice, bob, carol, dave, eve]
        a_list.sort()
        bob.value=15
        update_element_left(a_list,bob)
        assert a_list == [carol, alice, dave, bob, eve], \
            "The list should be  [(Carol, 13), (Alice, 14), (Dave, 14), (Bob, 15), (Eve, 15)] "
        bob.value = 14
        update_element_left(a_list, bob)
        assert a_list == [carol, bob, alice, dave, eve], \
            "The list should be  [(Carol, 13), (Bob, 14), (Alice, 14), (Dave, 14), (Eve, 15)] "
        bob.value = 13
        update_element_left(a_list, bob)
        assert a_list == [bob, carol, alice, dave,  eve], \
            "The list should be  [(Bob, 13), (Carol, 13), (Alice, 14), (Dave, 14), (Eve, 15)] "
        frank = Mate("Frank", "35")
        update_element_left(a_list, frank)
        assert a_list == [bob, carol, alice, dave, eve], \
            "The list should be  [(Bob, 13), (Carol, 13), (Alice, 14), (Dave, 14), (Eve, 15)] "

