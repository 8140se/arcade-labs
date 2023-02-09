"""Hi I'm Renata Bliss and I'm going to be your freestyle dance teacher."""
import arcade

arcade.open_window(512, 512, "Survey Program")

arcade.set_background_color(arcade.color.OCEAN_BOAT_BLUE)

arcade.start_render()
haocore = ((512/2+1-50 , 0),
           (512/2+1, 0),
           (512/2+1, 400),
           (512/2+1-50, 400))

arcade.draw_line(512/2+1, 0, 513/2+1, 400, arcade.color.BROWN, 100)
arcade.draw_lrtb_rectangle_outline(512/2+1, 512/2+1+50, 400, 0, arcade.color.OLD_GOLD, 3.55)
arcade.draw_polygon_outline(haocore, arcade.color.CHERRY_BLOSSOM_PINK, 2)


arcade.finish_render()
arcade.run()