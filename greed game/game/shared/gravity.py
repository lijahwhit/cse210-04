from game.shared.point import Point


class Gravity:
    """Handles global gravity
    The responsibility of Gravity is to hold the current rate of gravity, and return a velocity to apply to actors.
    Attributes:
        cell_size (int): For scaling gravity to grid.
        gravity (int): For controlling rate of gravity
    """

    def __init__(self, cell_size=1, gravity=1):
        """Constructs Gravity using the specified cell size.
        Args:
            cell_size (int): The size of a cell in the display grid.
            gravity (int): the current rate of gravity
        """
        self._cell_size = cell_size
        self._gravity = gravity

    def get_gravity_velocity(self):
        """Gets a velocity based on the current gravity rate
        Returns:
            Velocity: the calculated velocity
        """

        velocity = Point(0, self._gravity)
        velocity = velocity.scale(self._cell_size)

        return velocity