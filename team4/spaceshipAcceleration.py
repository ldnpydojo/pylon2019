from math import sin, cos, radians

HEIGHT = 600
WIDTH = 900

alien = Actor('player')

alien.pos = (500,500)

state = {
    "direction" : 0,
    "moving" : 0,
    "acceleration": 1
}
    
def draw():
    screen.fill((0, 0, 0))
    alien.draw()

def on_key_down(key):
    print(key)
    if key == keys.UP:
        state["moving"] = not state["moving"]
    elif key == keys.DOWN:
        state["moving"] = not state["moving"]
    
    print(alien.angle)

def update():
    if keyboard.RIGHT :
        alien.angle += 2
        state["direction"] = (state["direction"] - radians(alien.angle))
        state["acceleration"] = 10
    elif keyboard.LEFT:
        alien.angle -= 2
        state["direction"] = (state["direction"] + radians(alien.angle))
        state["acceleration"] = 10

    if state["moving"]:
        state["acceleration"] = min(state["acceleration"] + 2, 30)
        newX = sin(state["direction"])
        newY = cos(state["direction"])
        alien.x -= newX * state["acceleration"]
        alien.y -= newY * state["acceleration"]

    if alien.left < 0:
        alien.right = WIDTH
    if alien.right > WIDTH:
        alien.left = 0
    if alien.top < 0:
        alien.bottom = HEIGHT
    if alien.bottom > HEIGHT:
        alien.top = 0
