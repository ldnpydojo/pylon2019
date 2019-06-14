HEIGHT = 800
WIDTH = 400

ship = Actor('player_ship2_red')
ship.left = 0
ship.bottom = HEIGHT

enemy = Actor('enemy_black2.png')
enemy.left = 0
enemy.top = 0

def draw():
    # screen.fill((0, 0, 255))
    screen.blit('background', (0, 0))
    screen.blit('background', (0, 400))
    
    ship.draw()
    enemy.draw()

def update():
    if keyboard.left:
        ship.x -= 15
    if keyboard.right:
        ship.x += 15
    enemy.y += 10
    crash()

def crash():
    if enemy.colliderect(ship):
        sounds.death.play()
