import pytest
from exercises.mate import Mate
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



