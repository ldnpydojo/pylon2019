HEIGHT = 800
WIDTH = 400

ship = Actor('player_ship2_red')
ship.left = 0
ship.bottom = HEIGHT

enemy = Actor('enemy_black2.png')

enemy.left = 0
enemy.top = 0

bullets = []
enemies = []
enemies.append(enemy)


def draw():
    # screen.fill((0, 0, 255))
    screen.blit('background', (0, 0))
    screen.blit('background', (0, 400))
    
    ship.draw()
    for enemy in enemies:
        enemy.draw()

    for bullet in bullets:
    	bullet.draw()

def update():
    if keyboard.left:
        ship.x -= 15
    if keyboard.right:
        ship.x += 15
    for enemy in enemies:
        enemy.y += 1
    crash()

    for bullet in bullets:
    	bullet.y -= 10

    if ship.left > WIDTH:
        ship.left = 0

    if ship.right < 0:
        ship.right = WIDTH

def crash():
    for enemy in enemies:
        if enemy.colliderect(ship):
            sounds.death.play()
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                sounds.explosion.play()
                enemies.remove(enemy)
                bullets.remove(bullet)
            

def on_key_down(key):
    if key == keys.SPACE:
        bullet = Actor('bullet')
        bullets.append(bullet)
        bullet.left = ship.left
        bullet.top = ship.top + 5
