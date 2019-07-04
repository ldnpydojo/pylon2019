from math import sin, cos, radians

from offence_strategy import OffenceStrategy
import random

HEIGHT = 600
WIDTH = 900


number_0f_aliens = random.randint(1, 5)
offence_image = 'rock1'

aliens = []
offences = []

for i in range(number_0f_aliens):
    a = Actor(offence_image)
    offence = OffenceStrategy(actor=a, width=WIDTH, height=HEIGHT)
    aliens.append(a)
    offences.append(offence)


spaceship = Actor('player')

spaceship.pos = (500,500)

state = {
    "direction" : 0,
    "moving" : 0,
    "acceleration": 1
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
        state["acceleration"] = 10
    elif keyboard.LEFT:
        spaceship.angle -= 2
        state["direction"] = (state["direction"] + radians(spaceship.angle))
        state["acceleration"] = 10

    if state["moving"]:
        newX = sin(state["direction"])
        newY = cos(state["direction"])
        spaceship.x -= newX * state['acceleration']
        spaceship.y -= newY * state['acceleration']

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
