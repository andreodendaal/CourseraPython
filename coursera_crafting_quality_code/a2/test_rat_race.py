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

class Test_Maze(unittest.TestCase):

    def test_str(self):

        expected = "#######\n#.....#\n#.###.#\n#..@#.#\n#@#.@.#\n#######\nJ at (1, 1) ate 0 sprouts\nP at (1, 4) ate 0 sprouts"

        maze_1 = rat.Maze([['#', '#', '#', '#', '#', '#', '#'],
                            ['#', '.', '.', '.', '.', '.', '#'],
                            ['#', '.', '#', '#', '#', '.', '#'],
                            ['#', '.', '.', '@', '#', '.', '#'],
                            ['#', '@', '#', '.', '@', '.', '#'],
                            ['#', '#', '#', '#', '#', '#', '#']],
                            rat.Rat('J', 1, 1),
                            rat.Rat('P', 1, 4))

        #print(expected)
        #print(maze_1.__str__())

        self.assertEqual(expected, maze_1.__str__())

    def test_is_wall(self):

        is_wall = True
        not_wall = False

        maze_1 = rat.Maze([['#', '#', '#', '#', '#', '#', '#'],
                            ['#', '.', '.', '.', '.', '.', '#'],
                            ['#', '.', '#', '#', '#', '.', '#'],
                            ['#', '.', '.', '@', '#', '.', '#'],
                            ['#', '@', '#', '.', '@', '.', '#'],
                            ['#', '#', '#', '#', '#', '#', '#']],
                            rat.Rat('J', 1, 1),
                            rat.Rat('P', 1, 4))

        self.assertEqual(is_wall, maze_1.is_wall(1, 6))
        self.assertEqual(not_wall, maze_1.is_wall(2, 5))

    def test_character(self):
        rat1 = rat.Rat('J', 1, 1)
        rat2 = rat.Rat('P', 1, 4)


        maze_1 = rat.Maze([['#', '#', '#', '#', '#', '#', '#'],
                            ['#', '.', '.', '.', '.', '.', '#'],
                            ['#', '.', '#', '#', '#', '.', '#'],
                            ['#', '.', '.', '@', '#', '.', '#'],
                            ['#', '@', '#', '.', '@', '.', '#'],
                            ['#', '#', '#', '#', '#', '#', '#']],
                            rat1,
                            rat2)

        #Basic tests
        self.assertEqual('#', maze_1.get_character(0, 0))
        self.assertEqual('J', maze_1.get_character(1, 1))
        self.assertEqual('P', maze_1.get_character(1, 4))
        self.assertEqual('@', maze_1.get_character(4, 1))
        self.assertEqual('.', maze_1.get_character(4, 3))

