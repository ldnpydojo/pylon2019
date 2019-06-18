import numpy as np

# PyGame Zero Config
WIDTH = 800
HEIGHT = 600

# Game Objects. All module-scope.
ship = Actor('tship')
bullets = []
asteroids = []


class Config:
    """ Our Configuration Constants """
    center = (WIDTH / 2, HEIGHT / 2)
    bullet_velocity = 500
    asteroid_velocity = 250
    ship_turn_deg = 10
    ship_accel = 10
    ship_max_velocity = 1000
    ship_friction = 1
    timer = TIMEOUT = 5


def reset_ship():
    global ship
    ship.pos = Config.center
    ship.velocity = 0
    ship.angle = 0
    ship.draw_me = True


def reset():
    reset_ship()
    global asteroids
    asteroids = []
    global bullets
    bullets = []


# Start with a reset at module-load-time.
reset()


def new_bullet():
    bullet = Actor('tbullet')
    bullet.angle = ship.angle
    bullet.pos = ship.pos
    bullet.velocity = ship.velocity + Config.bullet_velocity
    bullet.draw_me = True
    return bullet


def add_bullet():
    b = new_bullet()
    bullets.append(b)


def new_asteroid():
    asteroid = Actor('asteroid')
    asteroid.pos = (np.random.randint(WIDTH),
                    np.random.randint(HEIGHT),)
    asteroid.angle = np.random.randint(180)
    asteroid.velocity = Config.asteroid_velocity
    asteroid.draw_me = True
    return asteroid


def add_asteroid():
    a = new_asteroid()
    asteroids.append(a)


def update_position(obj):
    """ Update x/y position of `obj`, based on its radial angle/velocity.
    Applies to all main game objects: ship, asteroids, bullets. """
    obj.x -= obj.velocity * np.sin(np.deg2rad(obj.angle)) / (2 * np.pi)
    obj.y -= obj.velocity * np.cos(np.deg2rad(obj.angle)) / (2 * np.pi)


def wrap(obj):
    """ Screen wrap-around for game-object `obj` """
    if obj.left > WIDTH:
        obj.right = 0
    elif obj.right < 0:
        obj.right = WIDTH
    elif obj.bottom < 0:
        obj.top = HEIGHT
    elif obj.top > HEIGHT:
        obj.bottom = 0


def on_key_down(key):
    """ Dedicated-press keys """
    if key == keys.SPACE:
        # Fire!
        add_bullet()
    elif key == keys.ESCAPE:
        # Reset Game State
        reset()


def read_keys():
    """ Read "holdable" keys """
    # Steering
    if keyboard.left:
        ship.angle += Config.ship_turn_deg
    if keyboard.right:
        ship.angle -= Config.ship_turn_deg

    # Thruster
    if keyboard.up:
        if ship.velocity < Config.ship_max_velocity - Config.ship_accel:
            ship.velocity += Config.ship_accel
        else:
            ship.velocity = Config.ship_max_velocity


def off_screen(obj):
    """ Screen wrap-around for game-object `obj` """
    if obj.left > WIDTH:
        return True
    elif obj.right < 0:
        return True
    elif obj.bottom < 0:
        return True
    elif obj.top > HEIGHT:
        return True
    return False


def retire(objs):
    """ Remove off-screen and inactive objects from list `objs`. """
    to_pop = []
    for (n, a) in enumerate(objs):
        if (not a.draw_me) or off_screen(a):
            to_pop.append(n)
    for n in to_pop[::-1]:
        objs.pop(n)


def draw():
    """ Primary Screen-Drawing Method.
    Called by PyGame Zero for every frame. """
    # Black background
    screen.fill((0, 0, 0))
    # Draw our main game objects: the ship, bullets, and asteroids
    ship.draw()
    for a in asteroids:
        a.draw()
    for b in bullets:
        b.draw()


def update():
    """ Primary object-update method
    Called by PyGame Zero for every frame. """
    # Read key input
    read_keys()

    # Update Positions
    update_position(ship)
    for b in bullets:
        update_position(b)
    for a in asteroids:
        update_position(a)

    # Detect collisions
    for a in asteroids:
        if a.colliderect(ship):
            # We don't actually have a "Game Over" behavior, yet.
            # Just print something to the console.
            print("SHOULD BE GAME OVER!!!")
        for b in bullets:
            if b.colliderect(a):
                print("SHOT AN ASTEROID!!!")
                a.draw_me = False
                b.draw_me = False

    # Ship Wrap-Around
    wrap(ship)
    # Retire off-screen stuff
    retire(asteroids)
    retire(bullets)

    # Timed Ops
    Config.timer -= 1
    if Config.timer == 0:
        # Dispatch a new asteroid
        add_asteroid()
        Config.timer = Config.TIMEOUT

    # "Frictional" Slow-Down
    if ship.velocity > 0:
        ship.velocity -= Config.ship_friction
