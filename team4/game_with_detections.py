from math import sin, cos, radians

from offence_strategy import OffenceStrategy
import random

HEIGHT = 600
WIDTH = 900


number_0f_aliens = random.randint(3, 5)
offence_image = 'rock1'

aliens = []
offences = []

spaceship = Actor('player')

for i in range(number_0f_aliens):
    a = Actor(offence_image)
    offence = OffenceStrategy(a, WIDTH, HEIGHT, spaceship)
    aliens.append(a)
    offences.append(offence)

spaceship.pos = (500,500)

state = {
    "direction" : 0,
    "moving" : 0
}

def draw():
    screen.fill((0, 0, 0))
    spaceship.draw()
    for alien in aliens:
        alien.draw()

def on_key_down(key):
    print(key)
    if key == keys.UP:
        state["moving"] = not state["moving"]
    elif key == keys.DOWN:
        state["moving"] = not state["moving"]

    print(spaceship.angle)

def update():
    if keyboard.RIGHT :
        spaceship.angle += 2
        state["direction"] = (state["direction"] - radians(spaceship.angle))
    elif keyboard.LEFT:
        spaceship.angle -= 2
        state["direction"] = (state["direction"] + radians(spaceship.angle))

    if state["moving"]:
        newX = sin(state["direction"])
        newY = cos(state["direction"])
        spaceship.x -= newX * 10
        spaceship.y -= newY * 10

    if spaceship.left < 0:
        spaceship.right = WIDTH
    if spaceship.right > WIDTH:
        spaceship.left = 0
    if spaceship.top < 0:
        spaceship.bottom = HEIGHT
    if spaceship.bottom > HEIGHT:
        spaceship.top = 0

    for offence in offences:
        offence.next_location()

    detect_collisions()

def detect_collisions():
    for offence in offences:
        if offence.detect_collision():
            sounds.eep.play()
