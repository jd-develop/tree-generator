#!/usr/bin/env python3
# coding:utf-8
import pygame
from tree import Tree, Grass

pygame.init()
pygame.display.set_caption(f"Tree generator")

screen = pygame.display.set_mode((800, 600))
screen.fill((127, 221, 76))


def generate_trees() -> tuple:
    return Tree(100), Tree(375), Tree(650)


tree, tree1, tree2 = generate_trees()
grass = Grass()

running = True

while running:
    screen.fill((127, 221, 76))
    screen.blit(tree.return_trunk()[0], tree.return_trunk()[1])
    screen.blit(tree1.return_trunk()[0], tree1.return_trunk()[1])
    screen.blit(tree2.return_trunk()[0], tree2.return_trunk()[1])
    screen.blit(grass.image, grass.rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            tree, tree1, tree2 = generate_trees()
