from game.casting.actor import Actor


class Meteoroid(Actor):
    """
    An item floating in space

    Meteoroids are either valuable ("gem"s), or not ("rock"s)

    Attributes:
        _type (String): "gem" or "rock"
    """

    def __init__(self):
        super().__init__()
        self._type = "rock"

    def get_type(self):
        """Gets the meteoroids's type

        Returns:
            string: The type.
        """
        return self._type

    def set_type(self, type):
        """Updates the type to the given one.

        Args:
            type (string): The given type.
        """
        self._type = type
