import pgzrun
import random
import ball

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

################################# Ball #################################


def center_ball_to_padd():
    ball.x = pad.centerx
    ball.y = pad.top - ball.radius - 1


center_ball_to_padd()
ball_is_moving = False

################################# Lives #################################
lives = 3

################################ PGZ Framework ################################


def on_key_down(key):
    if key == keys.SPACE:
        global ball_is_moving
        ball_is_moving = True


def update():
    global pad_velocity
    global ball_is_moving
    global lives
    global bricks
    global colors

    if keyboard.left and keyboard.right:
        pad_velocity = 0
    elif keyboard.left:
        if pad.left > 0:
            pad_velocity += PAD_ACC
            pad.centerx -= pad_velocity

            # check if pad has slightly gone offscreen
            if pad.left < 0:
                pad.left = 0

            if not ball_is_moving:
                center_ball_to_padd()

    elif keyboard.right:
        if pad.right < WIDTH:
            pad_velocity += PAD_ACC
            pad.centerx += pad_velocity

            # check if pad has slightly gone offscreen
            if pad.right > WIDTH:
                pad.right = WIDTH

            if not ball_is_moving:
                center_ball_to_padd()

    else:
        pad_velocity = 0

    if ball_is_moving:
        ball.move()

        if ball.x < ball.radius or ball.x > WIDTH - ball.radius:  # left or right wall
            ball.delta_x = -ball.delta_x

        if ball.y < ball.radius:  # top wall
            ball.delta_y = -ball.delta_y

        if ball.y < pad.top and pad.collidepoint((ball.x, ball.y + ball.radius)):  # pad collision
            # if the center of the ball is above the pad
            ball.delta_y = -ball.delta_y
            ball.y = pad.top - ball.radius

        check_bricks_collision()

        if ball.y > HEIGHT - ball.radius:  # bottom wall
            ball_is_moving = False
            center_ball_to_padd()
            ball.delta_x = abs(ball.delta_x)  # 2
            ball.delta_y = abs(ball.delta_y)  # 2

            # Lives system
            lives -= 1
            if lives == 0:
                lives = 3
                bricks = generate_bricks()
                colors = generate_colors()


def check_bricks_collision():
    for i in range(LINES):
        for j in range(COLUMNS):
            if bricks[i][j] is not None:
                left = ball.left(), ball.y
                right = ball.right(), ball.y
                top = ball.x, ball.top()
                bottom = ball.x, ball.bottom()

                if bricks[i][j].collidepoint(left) or bricks[i][j].collidepoint(right):
                    bricks[i][j] = None
                    ball.delta_x = -ball.delta_x
                elif bricks[i][j].collidepoint(top) or bricks[i][j].collidepoint(bottom):
                    bricks[i][j] = None
                    ball.delta_y = -ball.delta_y


def draw():
    screen.clear()
    screen.fill(BCKG_COLOR)
    for i in range(LINES):
        for j in range(COLUMNS):
            if bricks[i][j] is not None:
                screen.draw.filled_rect(bricks[i][j], colors[i][j])
    screen.draw.filled_rect(pad, pad_color)
    ball.draw(screen)
    screen.draw.text(f'Lives: {lives}', (10, 10))

pgzrun.go()
