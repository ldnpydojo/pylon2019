HEIGHT = 600
WIDTH = 900

RED = (128, 0, 0)
GREEN = (0, 128, 0)

player_one = Rect((20, 20), (50, 200))
player_two = Rect((WIDTH - 70, 20), (50, 200))

ball = Rect((WIDTH / 2, HEIGHT / 2), (50, 50))
ball_direction = [15, -20]

def draw():
    screen.fill(RED)
    screen.draw.filled_rect(player_one, GREEN)
    screen.draw.filled_rect(player_two, GREEN)
    screen.draw.filled_rect(ball, GREEN)

def update(unicode):
    ball.move_ip(*ball_direction)

    if ball.colliderect(player_one):
        ball_direction[0] *= -1

    if ball.colliderect(player_two):
        ball_direction[0] *= -1

    if not 0 < ball.y < HEIGHT:
        ball_direction[1] *= -1

    check_keys()

def check_keys():
    jump = 15
    if keyboard.q:
        player_one.y -= jump
    elif keyboard.a:
        player_one.y += jump

    elif keyboard.w:
        player_two.y -= jump
    elif keyboard.s:
        player_two.y += jump
