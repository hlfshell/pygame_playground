import pygame
from pygame.locals import *
from car import Car
from checkpoint import Checkpoint

class Game:
    def __init__(self):
        self._running = True
        self._display_surface = None
        self.size = self.width, self.height = 640, 400
        self._frame_per_sec = pygame.time.Clock()
        self._fps = 60

        self._cars : [Car] = pygame.sprite.Group()
        self._checkpoints : [Checkpoint] = pygame.sprite.Group()
        self._track = pygame.sprite.Group()

    def add_car(self, car : Car):
        self._cars.add(car)

    def add_checkpoint(self, checkpoint : Checkpoint):
        self._checkpoints.add(checkpoint)

    def on_init(self):
        pygame.init()
        self._display_surface = pygame.display.set_mode(self.size)
        self._running = True
        pygame.display.set_caption("Car Game")

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        for car in self._cars:
            car.move()
            # Calculate if the car impacts
            trackCollions = pygame.sprite.spritecollide(car, self._track, False)
            checkpointCollisions = pygame.sprite.spritecollide(car, self._checkpoints, False)
            for collision in checkpointCollisions:
                car.crash(collision)


    def on_render(self):
        self._display_surface.fill((0,0,0))
        for checkpoint in self._checkpoints:
            self._display_surface.blit(checkpoint.surface, checkpoint.rect)
        for car in self._cars:
            car.render()
            self._display_surface.blit(car.surf, car.rect)
        pygame.display.update()
        self._frame_per_sec.tick(self._fps)

    def on_cleanup(self):
        pass

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        
        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__":
    game = Game()
    car = Car("one", (20, 30))
    checkpoint = Checkpoint("abc123", (20, 20), (30, 30))
    game.add_car(car)
    game.add_checkpoint(checkpoint)
    game.on_execute()