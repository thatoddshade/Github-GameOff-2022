import pygame
from settings import *


class FallingFood:
    def __init__(self, x, y, food_type):
        # general setup
        self.type = food_type
        self.image = pygame.image.load(FOOD_DATA[self.type])

        self.position = [x, y]

        # transformation values
        self.rotation = 0
        self.width = self.image.get_width() * 2
        self.height = self.image.get_height() * 2

        # time
        self.falling_time = FOOD_FALLING_TIME
        self.drop_time = (
            pygame.time.get_ticks()
        )  # amount of ticks when food starts dropping

    def trans(self):
        # calculate new values
        if self.width > 10 and self.height > 10:
            self.width -= FOOD_TRANSFORMATION_VALUE
            self.height -= FOOD_TRANSFORMATION_VALUE
        self.rotation += FOOD_TRANSFORMATION_VALUE

        # apply values
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image = pygame.transform.rotate(self.image, self.rotation)
