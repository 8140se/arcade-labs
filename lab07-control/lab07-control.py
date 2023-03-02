import arcade
import math

SCREEN_WIDTH = 714
SCREEN_HEIGHT = 480


class Ball:
    """ This class manages a ball bouncing on the screen. """

    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        """ Constructor. """

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        """ Code to control the ball's movement. """

        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1

        if self.position_y < self.radius:
            self.change_y *= -1

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.change_y *= -1


class MyGame(arcade.Window):
    """ My window class. """

    def __init__(self, width, height, title):
        """ Constructor. """

        # Call the parent class's init function
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.ball = Ball(92, 92, 5, 6, 91, arcade.color.AUBURN)
        self.ball2 = Ball(300,200,4,6,91,arcade.color.BLEU_DE_FRANCE)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()
        self.ball2.draw()

    def update(self, delta_time):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.ball.update()
        self.ball2.update()
        if math.sqrt(math.pow(abs(self.ball.position_x - self.ball2.position_x),2) + math.pow(abs(self.ball.position_y - self.ball2.position_y),2)) <= self.ball.radius * 2:
            self.ball.change_x *= -1
            self.ball2.change_x *= -1
            self.ball.change_y *= -1
            self.ball2.change_y *= -1


def main():
    window = MyGame(714, 480, "Drawing Example")

    arcade.run()


main()