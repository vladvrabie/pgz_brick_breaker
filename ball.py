x = 0
y = 0
radius = 10
color = 0, 0, 255

delta_x = 2
delta_y = -2


def left():
    return x - radius


def right():
    return x + radius


def top():
    return y - radius


def bottom():
    return y + radius


def draw(screen):
    screen.draw.filled_circle((x, y), radius, color)


def move():
    global x, y
    x += delta_x
    y += delta_y
