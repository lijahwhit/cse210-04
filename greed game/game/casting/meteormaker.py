import random

from game.casting.gem import gem
from game.casting.rock import rock
from game.shared.point import Point
from game.casting.meteoroid import Meteoroid
from game.shared.color import Color


class Meteormaker:
    """Handles meteor creation
    The responsibility of Meteormaker is to handle the creation of new meteoroids
    Attributes:
        cell_size (int): For scaling gravity to grid.
        cols (int): For placing meteors in a random column
        font_size (int): For giving meteors the correct font size
        create_rate(int): For controlling likelyhood of new meteor being created
    """

    def __init__(self):
        """Constructs Gravity using the specified cell size.
        Args:
            cell_size (int): The size of a cell in the display grid.
            cols (int): The  number of columns in our actor grid
            font_size (int): Font size to assign meteors
            create_rate(int): % of how likely it is to create a new meteor         
        """

        self._create_rate = 14

    def update_rockmaker(self, cast):
        if random.randint(0, 100) > (100 - self._create_rate):
            rocks = rock().make_rock()
            cast.add_actor("rocksz", rocks)

    def update_gemmaker(self, cast):
        if random.randint(0, 100) > (100 - self._create_rate):
            gems = gem().make_gem()
            cast.add_actor("gems", gems)