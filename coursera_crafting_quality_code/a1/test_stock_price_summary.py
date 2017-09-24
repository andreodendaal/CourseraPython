import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    # Test Boundries
    def test_boundries(self):

    # Test all negative
        self.assertEqual(a1.stock_price_summary([-1, -0.01, -0.02, -0.2, -0.1, -0.33, -0.7]), (0.0, -2.36))

    # Test all positive
        self.assertEqual(a1.stock_price_summary([1, 0.01, 0.02, 0.2, 0.1, 0.33, 0.7]), (2.36, 0))

    # Test all 0
        self.assertEqual(a1.stock_price_summary([0, 0.00, 0.000, 0., 0, 0, 0]), (0, 0))

    # Test Size
    def test_size(self):
        self.assertEqual(a1.stock_price_summary([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]), (1.7, 0))

        self.assertEqual(a1.stock_price_summary([1000000, -1000000000000.00, 1000000, 1000000]), (3000000, -1000000000000))

        self.assertEqual(a1.stock_price_summary([]), (0, 0))

        self.assertEqual(a1.stock_price_summary([-1]), (0, -1))

        self.assertEqual(a1.stock_price_summary([1]), (1, 0))

    # Test Order
    def test_order(self):
        self.assertEqual(a1.stock_price_summary([-1, -1, -1, 1, 1, 1]), (3, -3))

        self.assertEqual(a1.stock_price_summary([1, 1, 1, -1, -1, -1]), (3, -3))

        self.assertEqual(a1.stock_price_summary([1, -1, 1, -1, 1, -1]), (3, -3))

        self.assertEqual(a1.stock_price_summary([-1, 1, -1, 1, -1, 1]), (3, -3))

        self.assertEqual(a1.stock_price_summary([-1, 1, -1, 1, -1, 1, -1]), (3, -4))

        self.assertEqual(a1.stock_price_summary([-1, 1, -1, 1, -1, 1, 1]), (4, -3))

    # Test Dichotomies
    def test_dichotomies(self):
        pass

if __name__ == '__main__':
    unittest.main(exit=False)