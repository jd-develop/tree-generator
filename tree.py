#!/usr/bin/env python3
# coding:utf-8
import pygame
import random


class Tree:
    def __init__(self, trunkx) -> None:
        self.trunk = Trunk(trunkx)
    
    def return_trunk(self):
        """ Retourne image, rect """
        return self.trunk.image, self.trunk.rect


class Leave:
    def __init__(self) -> None:
        pass


class Branch:
    def __init__(self) -> None:
        pass


class Trunk:
    def __init__(self, x) -> None:
        self.trunks = pygame.image.load('trunk.png')
        self.image = self.get_image(random.randint(0, 2))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 300
    
    def get_image(self, trunk):
        x = trunk * 50
        image = pygame.Surface([50, 189])
        image.blit(self.trunks, (0, 0), (x, 0, 50, 189))
        return image
