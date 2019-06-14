import random

HEIGHT = 800
WIDTH = 400

ship = Actor('player_ship2_red')
ship.left = 0
ship.bottom = HEIGHT



bullets = []
enemies = []

def new_enemy():
    enemy = Actor('enemy_black2.png')
    enemies.append(enemy)
    enemy.x = random.randint(0, WIDTH)
    enemy.speed = random.randint(5, 10)
    enemy.top = 0


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
    if random.randint(0, 30) == 0:
        new_enemy()
    for enemy in enemies:
        enemy.y += enemy.speed
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
