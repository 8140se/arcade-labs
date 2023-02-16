"""Hi I'm Renata Bliss and I'm going to be your freestyle dance teacher."""
import arcade

arcade.open_window(512, 512, "Survey Program")

#Fondo
arcade.set_background_color(arcade.color.PISTACHIO)

arcade.start_render()
MAX = 512+1
HALF = 512/2 + 1

#Listas de puntos usadas
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

pendulum = ((HALF-32, HALF),
            (HALF-12, HALF),
            (HALF+15, HALF-138),
            (HALF, HALF-140))

bg_lines = ((0, 0),
            (0, MAX),
            (MAX, 0),
            (MAX, MAX))

arcade.draw_lines(bg_lines, arcade.color.AMAZON, 110)
#Forma base
arcade.draw_lrtb_rectangle_filled(HALF-100, HALF+50, HALF+100, 0, (105, 28, 0))
arcade.draw_polygon_filled(polygon1, (105, 28, 0))
arcade.draw_polygon_filled(top_triangle, (105, 28, 0))
arcade.draw_polygon_filled(top_square, (54, 15, 1))
#Líneas que recorren los bordes de la estructura.
arcade.draw_line_strip(top_triangle_outline, arcade.color.OLD_GOLD, 2.5)
arcade.draw_lines(middle_outline, arcade.color.OLD_GOLD, 2.5)
arcade.draw_line_strip(back_outline, arcade.color.OLD_GOLD, 2.5)
#Círculo del reloj
arcade.draw_circle_filled(HALF-25, HALF+100, 53, (232, 227, 225))
#Ventana de cristal
arcade.draw_lrtb_rectangle_filled(HALF-70, HALF+25, HALF, -5, (13, 96, 140, 100))
#Péndulo
arcade.draw_polygon_filled(pendulum, arcade.color.OLD_GOLD)
arcade.draw_ellipse_filled(HALF+8, HALF-139, 40, 40, arcade.color.OLD_GOLD, 0)
#Rectángulo que "borra" el trozo de péndulo que se sale de la ventana y no pretende ser visto
arcade.draw_lrtb_rectangle_filled(HALF+25, HALF+30, HALF, 0, (54, 15, 1))
arcade.draw_lrtb_rectangle_filled(HALF-73, HALF-70, HALF, 0, (54, 15, 1))
arcade.draw_lrtb_rectangle_filled(HALF-73, HALF+30, HALF+2, HALF, (54, 15, 1))
#Reflejo del cristal
arcade.draw_polygon_filled(glass_reflection, (87, 147, 186,150))
arcade.draw_polygon_filled(glass_reflection2, (87, 147, 186,150))
arcade.draw_polygon_filled(glass_reflection3, (87, 147, 186,150))
#Números del reloj
arcade.draw_text("XII", HALF-33, HALF+137, arcade.color.BLACK, 10)
arcade.draw_text("III", HALF+12, HALF+93, arcade.color.BLACK, 10)
arcade.draw_text("VI", HALF-33, HALF+52, arcade.color.BLACK, 10)
arcade.draw_text("IX", HALF-73, HALF+93, arcade.color.BLACK, 10)
#Manillares
arcade.draw_line(HALF-28, HALF+100, HALF+12, HALF+90, arcade.color.BLACK, 3)
arcade.draw_line(HALF-28, HALF+100, HALF-28, HALF+74, arcade.color.BLACK, 3)
#Circunferencia parcial del reloj
arcade.draw_arc_outline(HALF-25, HALF+100, 106, 106, (54, 15, 1), 90, 270, 9, 120)
arcade.finish_render()
arcade.run()