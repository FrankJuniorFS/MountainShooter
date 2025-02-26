from abc import ABC, abstractmethod

import pygame


class Entity(ABC):
    def __init__(self, name: str, position: tuple[]):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png')
        self.surf = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self, ):
        pass