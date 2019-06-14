HEIGHT = 600
WIDTH = 900

alien = Actor('alien')

def draw():
    screen.fill((0, 128, 0))
    alien.draw()

def update():
    alien.x += 10

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        print("Eek!")
        alien.image = 'alien_hurt'
    else:
        print("You missed me!")
