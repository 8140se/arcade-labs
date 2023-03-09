import random
import arcade
# CONSTANTS
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_GOOD = 0.3
SPRITE_SCALING_BAD = 0.4
GOOD_COUNT = 30
BAD_COUNT = 25

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class FragmentRecollector(arcade.Window):
    """Custom window class"""

    def __init__(self):
        """Initializer"""
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Arcaea Fragment Recollector")

        #Sprite Lists
        self.player_list = None
        self.good_list = None
        self.bad_list = None

        #Player info
        self.player_sprite = None
        self.score = 0

        arcade.set_background_color(arcade.color.ROYAL_PURPLE)

    def setup(self):
        """ Set up the game and initialize the variables."""

        self.player_list = arcade.SpriteList()
        self.good_list = arcade.SpriteList()
        self.bad_list = arcade.SpriteList()
        self.score = 0

        self.player_sprite = arcade.Sprite("Hikari0_tired.png",SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 159
        self.player_sprite.center_y = 700
        self.player_list.append(self.player_sprite)

        #Create good and bad
        for i in range(GOOD_COUNT):
            good = arcade.Sprite("frag.png",SPRITE_SCALING_GOOD)

            good.center_x = random.randrange(SCREEN_WIDTH)
            good.center.y = random.randrange(SCREEN_HEIGHT)

            self.good_list.append(good)

        for i in range(BAD_COUNT):
            bad = arcade.Sprite("grievy af.png", SPRITE_SCALING_BAD)

            bad.center_x = random.randrange(SCREEN_WIDTH)
            bad.center.y = random.randrange(SCREEN_HEIGHT)

            self.bad_list.append(bad)
    def on_draw(self):
        """Draw everything"""
        arcade.start_render()
        self.good_list.draw()
        self.bad_list.draw()
        self.player_sprite.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_sprite.center_x += 3
        if key == arcade.key.RIGHT:
            self.player_sprite.center_x += -3
        if key == arcade.key.UP:
            self.player_sprite.center_y += 3
        if key == arcade.key.DOWN:
            self.player_sprite.center_y += -3

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.center_x += 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.center_y += 0

    def update(self, delta_time):
        self.bad_list.update()
        self.good_list.update()

        good_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.good_list)
        bad_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                            self.bad_list)
        for bad in bad_hit_list


