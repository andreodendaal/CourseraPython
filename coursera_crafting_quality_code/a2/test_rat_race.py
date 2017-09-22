import unittest
import a2 as rat


class Test_Rat(unittest.TestCase):

    def test_str(self):
        """Test get_divisors with 8 and [1, 2, 3]."""

        expected = "P at (1, 4) ate 0 sprouts"
        rat1 = rat.Rat('P', 1, 4)
        self.assertEqual(expected, rat1.__str__())

    def test_set_location(self):
        """Test set_location"""

        expected = "P at (10, 10) ate 0 sprouts"
        rat1 = rat.Rat('P', 1, 4)
        rat1.set_location(10, 10)
        self.assertEqual(expected, rat1.__str__())

    def test_eat_sprout(self):
        """Test set_location"""

        expected_1 = "P at (1, 4) ate 1 sprouts"
        expected_2 = "P at (1, 4) ate 2 sprouts"
        rat1 = rat.Rat('P', 1, 4)
        rat1.eat_sprout()
        self.assertEqual(expected_1, rat1.__str__())
        rat1.eat_sprout()
        self.assertEqual(expected_2, rat1.__str__())
