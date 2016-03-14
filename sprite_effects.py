__author__ = 'perkel666'

import pygame


def sprite_hover(sprite):
    if sprite.rect.collidepoint(pygame.mouse.get_pos()):
        sprite.image = sprite.image_hover
    else:
        if sprite.image != sprite.image_no_hover:
            sprite.image = sprite.image_no_hover


def sprite_pressed(sprite, events):
    #hover
    if sprite.rect.collidepoint(pygame.mouse.get_pos()):
        for event in events:
            # pressed
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                sprite.image = sprite.image_pressed
            # not pressed
            else:
                sprite.image = sprite.image_hover
    #no hover
    else:
        if sprite.image != sprite.image_no_hover:
            sprite.image = sprite.image_no_hover