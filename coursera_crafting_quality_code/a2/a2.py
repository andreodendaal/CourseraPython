# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    # Write your Rat methods here.

    def __init__(self, symbol, row, col):
        """
        (Rat, str, int, int) -> NoneType
     
        """
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row_new, col_new):
        """
        Rat, int, int) -> NoneType

        """
        self.row = row_new
        self.col = col_new


    def eat_sprout(self):
        """

        """
        self.num_sprouts_eaten += 1

    def __str__(self):
        """
        >>> rat1 = Rat('P', 1, 4)
        >>> rat1.__str__()
        P at (1, 4) ate 0 sprouts.

        """
        return "{0} at ({1}, {2}) ate {3} sprouts.".format(self.symbol, self.row, self.col, self.num_sprouts_eaten)


class Maze:

    """ A 2D maze. """

    # Write your Maze methods here.
    def __init__(self, maze_list, rat_1, rat_2):

        """
        (Maze, list of list of str, Rat, Rat) -> NoneType

        """
        self.maze_list = maze_list
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = 2

    def is_wall(self, row, col):

        """
        (Maze, int, int) -> bool
        >>>
  
        """

        if self.maze_list[row][col] == WALL:

            return True
        else:
            return False

    def get_character(self, row, col ):
        """
        (Maze, int, int) -> str
 
        """

        if self.rat_1.row == row and self.rat_1.col == col:
            character = RAT_1_CHAR
        elif self.rat_2.row == row and self.rat_2.col == col:
            character = RAT_2_CHAR
        elif self.maze_list[row][col] == '.':
            character = HALL
        elif self.maze_list[row][col] == '#':
            character = WALL
        elif self.maze_list[row][col] == '@':
            character = SPROUT

        return character

    def move(self, rat, vert, horz):
        """
        (Maze, Rat, int, int) ->bool

        """
        row = rat.row
        col = rat.col

        print('Before' + str(row), str(col))

        row = row + vert
        col = col + horz
        print('After ' + str(row), str(col))


    def __str__(self):
        """
        (Maze) -> str
 
        """

        str_list = ''
        for i in self.maze_list:
            str_elem = ''
            for elem in i:
                str_elem = str_elem + str(elem)

            str_list = str_list + str_elem + '\n'

        # add 1st rat
        rat_1_str = "{0} at ({1}, {2}) ate {3} sprouts".format(self.rat_1.symbol, self.rat_1.row,
                                                               self.rat_1.col, self.rat_1.num_sprouts_eaten)

        str_list = str_list + rat_1_str + '\n'
        # add 2nd rat
        rat_2_str = "{0} at ({1}, {2}) ate {3} sprouts".format(self.rat_2.symbol, self.rat_2.row,
                                                               self.rat_2.col, self.rat_2.num_sprouts_eaten)
        str_list = str_list + rat_2_str

        return str_list

