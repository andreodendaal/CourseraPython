import unittest
from a2 import get_length, is_longer, count_nucleotides, contains_sequence

class A2TestCase(unittest.TestCase):

    def test_get_length(self):
        self.assertEqual( get_length('ATCGAT'), 6)
        self.assertEqual( get_length('ATCG'), 4)
        self.assertEqual( get_length(''), 0)

    def test_is_longer(self):
        self.assertTrue(is_longer('ATCG', 'AT'))
        self.assertFalse(is_longer('ATCG', 'ATCGGA'))

    def test_count_nucleotides(self):
        self.assertEqual(count_nucleotides('ATCGGC', 'G'), 2)
        self.assertEqual(count_nucleotides('ATCTA', 'G'), 0)

    def test_contains_sequence(self):
        self.assertTrue(contains_sequence('ATCGGC', 'GG'))
        self.assertFalse(contains_sequence('ATCGGC', 'GT'))

if __name__ == '__main__':
    unittest.main