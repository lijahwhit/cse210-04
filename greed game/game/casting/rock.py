import random
from game.shared.point import Point
from game.casting.meteoroid import Meteoroid
from game.shared.color import Color

class rock():
    def __init__(self, cell_size=1, cols=1, font_size=1):
        
        self._cell_size = cell_size
        self._cols = cols
        self._font_size = font_size
        self._create_rate = 14
    
    
    def make_rock(self):
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
        
        meteoroid.set_type('rock')
        meteoroid.set_text('0')
        meteoroid.set_font_size(self._font_size)
        meteoroid.set_color(color)
        meteoroid.set_position(position)

        # returns it so Director can add it to the cast "meteoroids" group
        return meteoroid