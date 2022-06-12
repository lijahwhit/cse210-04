import random

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

    def __init__(self, cell_size=1, cols=1, font_size=1):
        """Constructs Gravity using the specified cell size.

        Args:
            cell_size (int): The size of a cell in the display grid.
            cols (int): The  number of columns in our actor grid
            font_size (int): Font size to assign meteors
            create_rate(int): % of how likely it is to create a new meteor         
        """
        self._cell_size = cell_size
        self._cols = cols
        self._font_size = font_size
        self._create_rate = 25

    def update_meteormaker(self, cast):
        if random.randint(0, 100) > (100 - self._create_rate):
            meteor = self.make_meteor()
            cast.add_actor("meteoroids", meteor)

    def make_meteor(self):
        """Creates a new meteor at the top of the screen

        Returns:
            reference to the new meteoroid
        """
        x = random.randint(1, self._cols - 1)
        y = 1
        position = Point(x, y)
        position = position.scale(self._cell_size)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        meteoroid = Meteoroid()
        type = random.choice([["rock", "0"], ["gem", "*"], ["gem2.0", "!"]])
        meteoroid.set_type(type[0])
        meteoroid.set_text(type[1])
        meteoroid.set_font_size(self._font_size)
        meteoroid.set_color(color)
        meteoroid.set_position(position)

        # returns it so Director can add it to the cast "meteoroids" group
        return meteoroid
