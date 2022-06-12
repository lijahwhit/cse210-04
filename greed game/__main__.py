
from game.casting.actor import Actor
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point
from game.shared.gravity import Gravity
from game.casting.meteormaker import Meteormaker

FRAME_RATE = 20
MAX_X = 1200
MAX_Y = 900
CELL_SIZE = 15
FONT_SIZE = 40
COLS = 80
ROWS = 60
CAPTION = "Greed"
WHITE = Color(255, 255, 255)


def main():

    # create the cast
    cast = Cast()

    # create the banner
    banner = Actor()
    banner.set_text("Collect Gems * to earn points!")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, CELL_SIZE))
    cast.add_actor("banners", banner)

    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y - (CELL_SIZE * 4))  # set the robot at the bottom
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)

    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    gravity = Gravity(CELL_SIZE)
    meteormaker = Meteormaker(CELL_SIZE, COLS, FONT_SIZE)
    director = Director(keyboard_service, video_service, gravity, meteormaker)
    director.start_game(cast)


if __name__ == "__main__":
    main()
