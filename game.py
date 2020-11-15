import pygame
from pygame.locals import *
from car import Car

class Game:
    def __init__(self):
        self._running = True
        self._display_surface = None
        self.size = self.width, self.height = 640, 400
        self._frame_per_sec = pygame.time.Clock()
        self._fps = 60

        self._cars : [Car] = pygame.sprite.Group()
        self._goals = pygame.sprite.Group()
        self._track = pygame.sprite.Group()

    def add_car(self, car : Car):
        self._cars.add(car)

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
            pygame.sprite.spritecollide(car, self._track, car.crash)
            pygame.sprit.spritecollide(car, self._goals, car.pass_goal)


    def on_render(self):
        self._display_surface.fill((0,0,0))
        for car in self._cars:
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
    game.add_car(car)
    game.on_execute()