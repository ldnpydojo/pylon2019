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
        set_alien_hurt()

def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 1.0)

def set_alien_normal():
    alien.image = 'alien'