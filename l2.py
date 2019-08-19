import pgzrun

################################# CONSTANTS #################################

WIDTH = 500
HEIGHT = 500

BCKG_COLOR = 127, 127, 127

LINES = 8
COLUMNS = 7

BRICK_WIDTH = 50
BRICK_HEIGHT = 20
BRICK_SIZE = BRICK_WIDTH, BRICK_HEIGHT

BRICK_H_DISTANCE = 5
BRICK_V_DISTANCE = 3

H_OFFSET = 40
V_OFFSET = 30

############################# Brick Generation #############################


def generate_bricks():
    bricks = []
    for i in range(LINES):
        line = []
        for j in range(COLUMNS):
            horizontal_pos = (BRICK_WIDTH + BRICK_H_DISTANCE) * j + H_OFFSET
            vertical_pos = (BRICK_HEIGHT + BRICK_V_DISTANCE) * i + V_OFFSET
            brick_pos = horizontal_pos, vertical_pos
            brick = Rect(brick_pos, BRICK_SIZE)
            line.append(brick)
        bricks.append(line)
    return bricks


bricks = generate_bricks()

################################# Colors #################################
color = 255, 0, 0

################################ PGZ Framework ################################


def draw():
    screen.clear()
    screen.fill(BCKG_COLOR)
    for i in range(LINES):
        for j in range(COLUMNS):
            screen.draw.filled_rect(bricks[i][j], color)


pgzrun.go()
