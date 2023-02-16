"""El siguiente programa dibuja lo único que me vino en mente."""
import arcade

MAX = 512+1
HALF = 512/2 + 1
arcade.open_window(512, 512, "UNDERTALE")


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

def draw_pendulo():
    """Dibuja el péndulo."""
    pendulum = ((HALF - 32, HALF),
                (HALF - 12, HALF),
                (HALF + 15, HALF - 138),
                (HALF, HALF - 140))

    arcade.draw_polygon_filled(pendulum, arcade.color.OLD_GOLD)
    arcade.draw_ellipse_filled(HALF+8, HALF-139, 40, 40, arcade.color.OLD_GOLD, 0)


def draw_reflejo():
    """Dibuja el resplandor del cristal."""
    glass_reflection = ((HALF - 70, HALF - 10),
                        (HALF - 70, HALF - 50),
                        (HALF + 25, HALF - 120),
                        (HALF + 25, HALF - 80))

    arcade.draw_polygon_filled(glass_reflection, (87, 147, 186,150))



def draw_agujas():
    """Dibuja las agujas del reloj."""
    arcade.draw_line(HALF-28, HALF+100, HALF+12, HALF+90, arcade.color.BLACK, 3)
    arcade.draw_line(HALF-28, HALF+100, HALF-28, HALF+74, arcade.color.BLACK, 3)



def draw_fondo():
    """Dibuja las lineas decorativas de fondo."""
    bg_lines = ((0, 0),
                (0, MAX),
                (MAX, 0),
                (MAX, MAX))

    arcade.draw_lines(bg_lines, arcade.color.AMAZON, 110)

def circunferencia():
    """Dibuja la circunferencia que rodea el reloj."""
    # Circunferencia parcial del reloj
    arcade.draw_arc_outline(HALF - 25, HALF + 100, 106, 106, (54, 15, 1), 90, 270, 9, 120)
def ventana():
    """Dibuja la ventana."""
    arcade.draw_lrtb_rectangle_filled(HALF - 70, HALF + 25, HALF, -5, (13, 96, 140, 100))
    # Rectángulo que "borra" el trozo de péndulo que se sale de la ventana y no pretende ser visto
    arcade.draw_lrtb_rectangle_filled(HALF + 25, HALF + 30, HALF, 0, (54, 15, 1))
    arcade.draw_lrtb_rectangle_filled(HALF - 73, HALF - 70, HALF, 0, (54, 15, 1))
    arcade.draw_lrtb_rectangle_filled(HALF - 73, HALF + 30, HALF + 2, HALF, (54, 15, 1))

def main():
    """Anyhting that doesn't move or is unique. Base Drawing."""

    #Color del fondo
    arcade.set_background_color(arcade.color.PISTACHIO)
    arcade.start_render()

    # Forma base
    arcade.draw_lrtb_rectangle_filled(HALF - 100, HALF + 50, HALF + 100, 0, (105, 28, 0))
    arcade.draw_polygon_filled(polygon1, (105, 28, 0))
    arcade.draw_polygon_filled(top_triangle, (105, 28, 0))
    arcade.draw_polygon_filled(top_square, (54, 15, 1))

    # Líneas que recorren los bordes de la estructura.
    arcade.draw_line_strip(top_triangle_outline, arcade.color.OLD_GOLD, 2.5)
    arcade.draw_lines(middle_outline, arcade.color.OLD_GOLD, 2.5)
    arcade.draw_line_strip(back_outline, arcade.color.OLD_GOLD, 2.5)

    # Círculo del reloj
    arcade.draw_circle_filled(HALF - 25, HALF + 100, 53, (232, 227, 225))


    # Números del reloj
    arcade.draw_text("XII", HALF - 33, HALF + 137, arcade.color.BLACK, 10)
    arcade.draw_text("III", HALF + 12, HALF + 93, arcade.color.BLACK, 10)
    arcade.draw_text("VI", HALF - 33, HALF + 52, arcade.color.BLACK, 10)
    arcade.draw_text("IX", HALF - 73, HALF + 93, arcade.color.BLACK, 10)

main()
draw_fondo()
draw_agujas()
draw_pendulo()
ventana()
circunferencia()
draw_reflejo()

arcade.finish_render()
arcade.run()
