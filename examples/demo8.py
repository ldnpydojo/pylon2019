HEIGHT = 600
WIDTH = 900

dojo = Actor('dojo')


def draw():
    screen.fill((255, 255, 255))
    dojo.draw()


def update():
    dojo.angle += 20
