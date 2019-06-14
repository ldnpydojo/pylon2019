HEIGHT = 800
WIDTH = 400

ship = Actor('player_ship2_red')

def draw():
    screen.fill((0, 0, 255))
    ship.left = 0
    ship.bottom = HEIGHT
    ship.draw()
