#!/usr/bin/env python3
# coding:utf-8
import pygame
from tree import Tree

pygame.init()
pygame.display.set_caption(f"Tree generator")

screen = pygame.display.set_mode((800, 600))
screen.fill((127, 221, 76))

running = True
tree = Tree(100)
tree1 = Tree(375)
tree2 = Tree(650)

while running:
    screen.fill((127, 221, 76))
    screen.blit(tree.return_trunk()[0], tree.return_trunk()[1])
    screen.blit(tree1.return_trunk()[0], tree1.return_trunk()[1])
    screen.blit(tree2.return_trunk()[0], tree2.return_trunk()[1])
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            tree = Tree(100)
            tree1 = Tree(375)
            tree2 = Tree(650)
