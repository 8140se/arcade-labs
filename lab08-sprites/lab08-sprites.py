import random
import arcade
# CONSTANTS
SPRITE_SCALING_PLAYER = 0.1
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

        self.sound = arcade.load_sound("laser.wav")
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
        self.player_sprite.center_y = 600
        self.player_list.append(self.player_sprite)

        #Create good and bad
        for i in range(GOOD_COUNT):
            good = arcade.Sprite("frag.png",SPRITE_SCALING_GOOD)

            good.center_x = random.randrange(SCREEN_WIDTH)
            good.center_y = random.randrange(SCREEN_HEIGHT)
            good.change_x += 2 * random.choice([-1,1])
            good.change_y += 2 * random.choice([-1, 1])

            self.good_list.append(good)

        for i in range(BAD_COUNT):
            bad = arcade.Sprite("grievy af.png", SPRITE_SCALING_BAD)

            bad.center_x = random.randrange(SCREEN_WIDTH)
            bad.center_y = random.randrange(SCREEN_HEIGHT)
            bad.change_x += 0.5 * random.choice([-1, 1])
            bad.change_y += 0.5 * random.choice([-1, 1])

            self.bad_list.append(bad)
    def on_draw(self):
        """Draw everything"""
        arcade.start_render()
        self.good_list.draw()
        self.bad_list.draw()
        self.player_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        if len(self.good_list) == 0:
            arcade.draw_text("GAME OVER",200,400,arcade.color.WHITE,50)
            arcade.draw_text("Your total score is "+str(self.score), 250, 300, arcade.color.WHITE, 25)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_sprite.change_x += -5
        if key == arcade.key.RIGHT:
            self.player_sprite.change_x += +5
        if key == arcade.key.UP:
            self.player_sprite.change_y += 5
        if key == arcade.key.DOWN:
            self.player_sprite.change_y += -5

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0

    def update(self, delta_time):
        self.bad_list.update()
        self.good_list.update()
        self.player_list.update()

        good_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.good_list)
        bad_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                            self.bad_list)
        for bad in bad_hit_list:
            bad.remove_from_sprite_lists()
            arcade.play_sound(self.sound)
            if self.score == 0:
                self.score = 0
            else:
                self.score -= 2

        for good in good_hit_list:
            good.remove_from_sprite_lists()
            self.score += 1

        for good in self.good_list:
            if good.center_x >= SCREEN_WIDTH or good.center_x <= 0:
                good.change_x *=(-1)
            if good.center_y >= SCREEN_HEIGHT or good.center_y <= 0:
                good.change_y *= (-1)

        for bad in self.bad_list:
            if bad.center_x >= SCREEN_WIDTH or bad.center_x <= 0:
                bad.change_x *=(-1)
            if bad.center_y >= SCREEN_HEIGHT or bad.center_y <= 0:
                bad.change_y *= (-1)
            if len(self.good_list) == 0:
                bad.change_y=0
                bad.change_x=0





def main():
    window = FragmentRecollector()
    window.setup()
    arcade.run()

main()