
from game.shared.color import Color
white = Color(255, 255, 255)
red = Color(255, 0, 0)


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
        _gravity (Gravity): For controlling gravity rate and calculating gravity velocities
    """

    def __init__(self, keyboard_service, video_service, gravity, meteormaker):
        """Constructs a new Director using the specified keyboard and video services.

        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
            gravity (Gravity): An instance of Gravity
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._gravity = gravity
        self._meteormaker = meteormaker
        self._score = 0

    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.

        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with meteoroids.

        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        meteoroids = cast.get_actors("meteoroids")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)

        for meteoroid in meteoroids:

            # get gravity velocity to apply to meteoroids
            gravity_velocity = self._gravity.get_gravity_velocity()
            meteoroid.set_velocity(gravity_velocity)
            # apply gravity to all meteoroids to move them downward
            meteoroid.move_next(max_x, max_y*2)

            # update score and clarify catch
            if meteoroid.get_position().get_y() > max_y:
                cast.remove_actor("meteoroids", meteoroid)

            # check for collision with robot
            if robot.get_position().equals(meteoroid.get_position()):
                # remove the meteoroid

                # check the meteoroids _get_type and then apply score accordingly

                if meteoroid.get_type() == "rock":
                    self._score -= 10

                elif meteoroid.get_type() == "gem":
                    self._score += 5
                    
                elif meteoroid.get_type() == "gem2.0":
                    self._score += 10

                if self._score >= 0:
                    banner.set_color(white)
                else:
                    banner.set_color(red)

                # display new score
                banner.set_text(f"Score: {self._score}")

                # remove that meteoroid
                cast.remove_actor("meteoroids", meteoroid)

        # randomly generate some new meteoroids
        self._meteormaker.update_meteormaker(cast)

    def _do_outputs(self, cast):
        """Draws the actors on the screen.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
