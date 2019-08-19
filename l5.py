import pgzrun
import random

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


def random_color():
    r = random.randrange(50, 256)
    g = random.randrange(50, 256)
    b = random.randrange(50, 256)
    return r, g, b


def generate_colors():
    colors = []
    for i in range(LINES):
        line = []
        for j in range(COLUMNS):
            line.append(random_color())
        colors.append(line)
    return colors


colors = generate_colors()

################################# Pad #################################

pad_size = 120, 15
PAD_V_OFFSET = 50
pad = Rect((WIDTH // 2 - pad_size[0] // 2, HEIGHT - PAD_V_OFFSET), pad_size)

pad_color = 0, 0, 0

PAD_ACC = 1
pad_velocity = 0

################################ PGZ Framework ################################


def update():
    global pad_velocity

    if keyboard.left and keyboard.right:
        pad_velocity = 0
    elif keyboard.left:
        if pad.left > 0:
            pad_velocity += PAD_ACC
            pad.centerx -= pad_velocity

            # check if pad has slightly gone offscreen
            if pad.left < 0:
                pad.left = 0

    elif keyboard.right:
        if pad.right < WIDTH:
            pad_velocity += PAD_ACC
            pad.centerx += pad_velocity

            # check if pad has slightly gone offscreen
            if pad.right > WIDTH:
                pad.right = WIDTH

    else:
        pad_velocity = 0


def draw():
    screen.clear()
    screen.fill(BCKG_COLOR)
    for i in range(LINES):
        for j in range(COLUMNS):
            screen.draw.filled_rect(bricks[i][j], colors[i][j])
    screen.draw.filled_rect(pad, pad_color)


pgzrun.go()
