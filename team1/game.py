HEIGHT = 800
WIDTH = 400

ship = Actor('player_ship2_red')
ship.left = 0
ship.bottom = HEIGHT

def draw():
    # screen.fill((0, 0, 255))
    screen.blit('background', (0, 0))
    screen.blit('background', (0, 400))
    
    ship.draw()

def update():
    if keyboard.left:
        ship.x -= 15
    if keyboard.right:
        ship.x += 15