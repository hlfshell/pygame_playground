import pygame
vector = pygame.math.Vector2
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN

class Car(pygame.sprite.Sprite):

    def __init__(
        self, id : str,
        position : (int, int),
        orientation : int = 0
        ):
        super().__init__()

        self._id = id
        self._position = position
        self._orientation = orientation

        self._radius = 3

        self._color = (128, 255, 40)

        self.surf = pygame.Surface(self._position)
        self.surf.fill(self._color)
        self.rect = self.surf.get_rect(center = self._position)
    
        self._velocity = vector(0,0)
        self._acceleration = vector(0,0)

        self._score = 0

    def move(self):
        self._acceleration = vector(0,0)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self._acceleration.x = -0.5
        elif pressed_keys[K_RIGHT]:
            self._acceleration.x = 0.5
        else:
            self._acceleration.x = 0.0

        if pressed_keys[K_UP]:
            self._acceleration.y = -0.5
        elif pressed_keys[K_DOWN]:
            self._acceleration.y = +0.5
        else:
            self._acceleration.y = 0.0

        self._velocity += self._acceleration
        offset = self._velocity + (0.5 * self._acceleration)
        # if position[0] < 0.0:
        #     position[0] = 0.0
        # elif position[0] > 1.0:
        #     position[1] = 0

        self._position += offset

        # self.rect.midbottom = self._position
        self.rect = self.rect.move(offset[0], offset[1])

    def crash(self, test):
        print(test)
        self._score += -100

    def pass_goal(self):
        print(locals())