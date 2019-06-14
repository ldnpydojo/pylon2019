HEIGHT = 600
WIDTH = 900

alien = Actor('alien')

def draw():
    screen.fill((0, 128, 0))
    alien.draw()

def update():
    alien.x += 20
