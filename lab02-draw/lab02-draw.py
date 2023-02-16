"""Hi I'm Renata Bliss and I'm going to be your freestyle dance teacher."""
import arcade

arcade.open_window(512, 512, "Survey Program")

arcade.set_background_color(arcade.color.OCEAN_BOAT_BLUE)

arcade.start_render()
MAX= 512+1
HALF= 512/2 + 1
arcade.draw_lrtb_rectangle_filled(HALF-100, HALF+50, HALF+100, 0, arcade.color.BROWN)

glass_reflection = ((HALF-70, HALF-10),
                    (HALF-70, HALF-50),
                    (HALF+25, HALF-120),
                    (HALF+25, HALF-80))

glass_reflection2 = ((HALF-70, HALF-110),
                    (HALF-70, HALF-150),
                    (HALF+25, HALF-220),
                    (HALF+25, HALF-180))

glass_reflection3 = ((HALF-70, HALF-210),
                    (HALF-70, HALF-250),
                    (HALF+25, HALF-320),
                    (HALF+25, HALF-280))

middle_outline = ((HALF-100, -5),
                  (HALF-100, HALF+100),
                  (HALF+50, -5),
                  (HALF+50, HALF+100))

back_outline = ((HALF-25, HALF+230),
                (HALF+15, HALF+269),
                (HALF+90, HALF+147),
                (HALF+90, -5))

polygon1 =((HALF+50, 0),
          (HALF+50, HALF+100),
          (HALF+90, HALF+147),
          (HALF+90, 0))

top = ((HALF-100, HALF+100),
       (HALF+50, HALF+100),
       (HALF+90, HALF+147),
       (HALF-60, HALF+147))

top_triangle = ((HALF-100, HALF+100),
                (HALF+50, HALF+100),
                (HALF-25, HALF+230))

top_triangle_outline = ((HALF-100, HALF+100),
                        (HALF-25, HALF+230),
                        (HALF+50, HALF+100))

top_square = ((HALF-25, HALF+230),
              (HALF+50, HALF+100),
              (HALF+90, HALF+147),
              (HALF+15, HALF+269))

arcade.draw_polygon_filled(polygon1, arcade.color.BROWN)
arcade.draw_polygon_filled(top, arcade.color.DARK_BROWN)
arcade.draw_polygon_filled(top_triangle, arcade.color.BROWN)
arcade.draw_polygon_filled(top_square, arcade.color.DARK_BROWN)
arcade.draw_line_strip(top_triangle_outline, arcade.color.OLD_GOLD, 2.5)
arcade.draw_lines(middle_outline, arcade.color.OLD_GOLD, 2.5)
arcade.draw_line_strip(back_outline, arcade.color.OLD_GOLD, 2.5)
arcade.draw_circle_filled(HALF-25, HALF+100, 53, arcade.color.WHITE_SMOKE)
arcade.draw_arc_outline(HALF-25, HALF+100, 106, 106, arcade.color.DARK_BROWN, 90, 270, 9, 120)
arcade.draw_lrtb_rectangle_filled(HALF-70, HALF+25, HALF, -5, (13, 96, 140, 100))


arcade.draw_polygon_filled(glass_reflection, (87, 147, 186,150))
arcade.draw_polygon_filled(glass_reflection2, (87, 147, 186,150))
arcade.draw_polygon_filled(glass_reflection3, (87, 147, 186,150))
arcade.finish_render()
arcade.run()