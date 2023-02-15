"""Hi I'm Renata Bliss and I'm going to be your freestyle dance teacher."""
import arcade

arcade.open_window(512, 512, "Survey Program")

arcade.set_background_color(arcade.color.OCEAN_BOAT_BLUE)

arcade.start_render()
MAX= 512+1
HALF= 512/2 + 1
arcade.draw_lrtb_rectangle_filled(HALF-100, HALF+50, HALF+100, 0, arcade.color.BROWN)

arcade.draw_lrtb_rectangle_outline(HALF-100, HALF+50, HALF+100, -5, arcade.color.OLD_GOLD, 3)

polygon1 =((HALF+50, 0),
          (HALF+50, HALF+100),
          (HALF+90, HALF+147),
          (HALF+90, 0))

top = ((HALF-100, HALF+100),
       (HALF+50, HALF+100),
       (HALF+90, HALF+147),
       (HALF-60, HALF+147))

arcade.draw_polygon_filled(polygon1, arcade.color.BROWN)
arcade.draw_polygon_filled(top, arcade.color.BRONZE)
arcade.finish_render()
arcade.run()