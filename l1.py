import pgzrun

WIDTH = 500
HEIGHT = 500

size = 100, 100
poz = 100, 100

brick = Rect(poz, size)

color = 255, 0, 0


def draw():
    screen.draw.filled_rect(brick, color)


pgzrun.go()
