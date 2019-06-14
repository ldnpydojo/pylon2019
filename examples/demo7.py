HEIGHT = 600
WIDTH = 900

alien = Actor('alien')

def draw():
    screen.fill((0, 128, 0))
    alien.draw()

def update():
    alien.x += 20
    if alien.left > WIDTH:
        alien.right = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()

def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()

def set_alien_normal():
    alien.image = 'alien'