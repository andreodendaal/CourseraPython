import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    # Test Boundries
    def test_boundries(self):

        nums = [1, 2, 3, 4, 5, 6]
        nums_after = [6, 2, 3, 4, 5, 1]
        a1.swap_k(nums, 1)

        self.assertEqual(nums, nums_after)

        nums = [1, 2, 3, 4, 5, 6, 7]
        nums_after = [5, 6, 7, 4, 1, 2, 3]

        # edge of Precondtion: 0 <= k <= len(L) // 2
        a1.swap_k(nums, 3)

        self.assertEqual(nums, nums_after)

    # Test Size
    def test_size(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
        nums_after = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 11 ,1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
        a1.swap_k(nums, 10)

        self.assertEqual(nums, nums_after)

    def test_order(self):
        strs = ['E', 'F', 'C', 'D', 'A', 'B']
        strs_after = ['A', 'B', 'C', 'D', 'E', 'F']
        a1.swap_k(strs_after, 2)
    #
        self.assertEqual(strs, strs_after)
    # test strings
    def test_dichotomies(self):
        strs = ['A', 'B', 'C', 'D', 'E', 'F']
        strs_after = ['E', 'F', 'C', 'D', 'A', 'B']
        a1.swap_k(strs, 2)

        self.assertEqual(strs, strs_after)

    def test_dichotomies(self):
        mix = [1, 'B', 2, 'D', 3, 'F']
        mix_after = [3, 'F', 2, 'D', 1, 'B']
        a1.swap_k(mix, 2)

        self.assertEqual(mix, mix_after)
        
if __name__ == '__main__':
    unittest.main(exit=False)