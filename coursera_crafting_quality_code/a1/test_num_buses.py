import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.

    # Test Boundries
    def test_boundries(self):

        ''''
        Test with 1 Person, expect 1 bus
        '''
        self.assertEqual(a1.num_buses(1), 1)
        '''
        Test with 0 People, expect 0 bus
        '''
        self.assertEqual(a1.num_buses(0), 0)
        '''
        Test with 50 People (max for 1 bus)
        '''
        self.assertEqual(a1.num_buses(50), 1)
        '''
        Test with 51 People (max for 1 bus is 50, expect 2)
        '''
        self.assertEqual(a1.num_buses(51), 2)
        '''
        Test with 49 People (max for 1 bus is 50, expect 1)
        '''
        self.assertEqual(a1.num_buses(49), 1)

    # Test Size
    def test_size(self):

        '''
        Test for extreme size 1000 000 people, expect 20 000
        '''
        self.assertEqual(a1.num_buses(1000000), 20000)


    # Test Dichotomies
    def test_dichotomies(self):
        '''
        Test for odd num people 33, expect 1
        '''
        self.assertEqual(a1.num_buses(33), 1)
        '''
        Test for fraction num people 50.5, expect 2
        '''
        self.assertEqual(a1.num_buses(50.5), 2)
        '''
        Test for fraction num people .5, expect 1
        '''
        self.assertEqual(a1.num_buses(.5), 1)

    # Test Order
    def test_order(self):
        pass

if __name__ == '__main__':
    unittest.main(exit=False)