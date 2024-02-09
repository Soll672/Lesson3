import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "My Arcade Game"


class Falcon(arcade.Sprite):
    def __init__(self):
        super().__init__('falcon.png', 0.3)
        self.center_x = SCREEN_WIDTH / 2

        self.center_y = 100
class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture('background.jpg')
        self.falcon = Falcon()
        self.setup()

    def setup(self):
        pass

    def on_draw(self):
        self.clear((255, 255, 255))
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT,
                                      self.bg)
        self.falcon.draw()
    def update(self, delta_time: float):
        pass


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()
