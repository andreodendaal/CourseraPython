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
        return "{0} at ({1}, {2}) ate {3} sprouts".format(self.symbol, self.row, self.col, self.num_sprouts_eaten)



class Maze:

    """ A 2D maze. """

    # Write your Maze methods here.
    def __init__(self, maze_list, Rat):

        """
        (Maze, list of list of str, Rat, Rat) -> NoneType

        """
        pass

    def is_wall(self, int1, int2):

        """
        (Maze, int, int) -> bool
  
        """
        pass

    def get_character(self, int1, int2 ):
        """
        (Maze, int, int) -> str
 
        """
        pass

    def move(self, Rat, int1, int2):
        """
        (Maze, Rat, int, int) ->bool

        """
        pass

    def ___str___(self):
        """
        (Maze) -> str
 
        """
        pass

print(Rat('P', 1, 4))
