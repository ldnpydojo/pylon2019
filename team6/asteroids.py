import pgzrun
import random
HEIGHT = 600
WIDTH = 1000

spaceship = Actor('spaceship')
spaceship.x = WIDTH / 2
spaceship.y = HEIGHT - 20
spaceship.angle = 180

spaceship.x_increment = 0
spaceship.y_increment = 0
spaceship.fire_direction = (0, -5)
spaceship.fire_location = lambda: spaceship.midtop

asteroid = Actor("asteroid.png")
asteroid.x = random.randint(20, WIDTH-20)
asteroid.bottom = random.randint(asteroid.height, HEIGHT-40)
asteroid.x_velocity = random.randint(-2, 2)
asteroid.y_velocity = random.randint(-2, 2)

bullet = None

playing = True
score = 0


def update():
    global playing, bullet, asteroid, score
    if playing:
        spaceship.x = (spaceship.x + spaceship.x_increment) % WIDTH
        spaceship.y = (spaceship.y + spaceship.y_increment) % HEIGHT
        #
    if asteroid:
        asteroid.x += asteroid.x_velocity
        asteroid.y += asteroid.y_velocity
        if asteroid.y > HEIGHT:
            asteroid.y -= HEIGHT
        if asteroid.y < 0:
            asteroid.y += HEIGHT
        if asteroid.x > WIDTH:
            asteroid.x -= WIDTH
        if asteroid.x < 0:
            asteroid.x += WIDTH
        if asteroid.colliderect(spaceship):
            spaceship.image = "crashed_spaceship"
            sounds.bomb.play()
            playing = False
    if bullet:
        bullet.x += bullet.x_velocity
        bullet.y += bullet.y_velocity
        if asteroid and bullet.colliderect(asteroid):
            sounds.blast.play()
            asteroid.x = random.randint(20, WIDTH - 20)
            asteroid.bottom = random.randint(asteroid.height, HEIGHT - 40)
            asteroid.x_velocity = random.randint(-4, 4)
            asteroid.y_velocity = random.randint(-4, 4)
            bullet = None
            score += 1

def draw():
    """Redraw the screen."""
    screen.fill((0,0,0))
    spaceship.draw()
    if asteroid:
        asteroid.draw()
    if not playing:
        screen.draw.text('Game Over', (WIDTH/2, HEIGHT/2))
    screen.draw.text('Score: % s' % (score * 50), (20, 20))
    if bullet:
        bullet.draw()

def on_key_down(key):
    global bullet
    if not playing:
        return
    if key == keys.UP:
        spaceship.angle = 180
        spaceship.y_increment = -2
        spaceship.fire_direction = (0, -5)
        spaceship.fire_location = lambda: spaceship.midtop
    elif key == keys.DOWN:
        spaceship.angle = 0
        spaceship.y_increment = 2
        spaceship.fire_direction = (0, 5)
        spaceship.fire_location = lambda: spaceship.midbottom
    elif key == keys.RIGHT:
        spaceship.angle = 90
        spaceship.x_increment = 2
        spaceship.fire_direction = (5, 0)
        spaceship.fire_location = lambda: spaceship.midright
    elif key == keys.LEFT:
        spaceship.angle = 270
        spaceship.x_increment = -2
        spaceship.fire_direction = (-5, 0)
        spaceship.fire_location = lambda: spaceship.midleft
    elif key == keys.SPACE:
        bullet = Actor('bullet', spaceship.fire_location())
        bullet.x_velocity = spaceship.fire_direction[0]
        bullet.y_velocity = spaceship.fire_direction[1]
        music.play_once("laser5")


def on_key_up():
    spaceship.x_increment = 0
    spaceship.y_increment = 0

pgzrun.go()
