import random


class OffenceStrategy:
    initial_free_zone_width = 250
    initial_free_zone_height = 250

    def __init__(self, actor, width, height, spaceship):
        self._actor = actor
        self._rand_range_min = 1
        self._rand_range_max = 3
        self._width = width
        self._height = height
        self._spaceship = spaceship

        half_free_zone = OffenceStrategy.initial_free_zone_width / 2
        if self.get_sign() > 0.0:
            initial_x = random.randint(0, self._width / 2 - half_free_zone )
        else:
            initial_x = random.randint(self._width / 2 + half_free_zone, self._width)

        if self.get_sign() > 0.0:
            initial_y = random.randint(0, self._height / 2 - half_free_zone)
        else:
            initial_y = random.randint(self._height / 2 + half_free_zone, self._height)

        self._actor.x = initial_x
        self._actor.y = initial_y


    def get_step(self):
        return random.randint(self._rand_range_min, self._rand_range_max)

    def get_sign(self):
        if random.randint(0, 1) > 0.5:
            return 1.0
        else:
            return -1.0

    def next_location(self):
        sign_x = self.get_sign()
        sign_y = self.get_sign()
        step_x = self._actor.x + sign_x * self.get_step()
        step_y = self._actor.y + sign_y * self.get_step()

        if self._actor.left > self._width:
            step_x = -self._actor.width + 1

        if self._actor.right < 0.0:
            step_x = self._width

        if self._actor.top > self._height:
            step_y = 1.0 - self._actor.height

        if self._actor.bottom < 0.0:
            step_y = self._height

        self._actor.x = step_x
        self._actor.y = step_y


        return (step_x, step_y)

    def detect_collision(self):
        is_collision = self._spaceship.collidepoint((self._actor.x, self._actor.y))

        return is_collision