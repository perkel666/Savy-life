__author__ = 'perkel666'

import pygame

def sprite_hover(sprite):
    if sprite.rect.collidepoint(pygame.mouse.get_pos()):
                    sprite.image = sprite.image_hover
    else:
        if sprite.image != sprite.image_no_hover:
            sprite.image = sprite.image_no_hover