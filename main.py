__author__ = 'perkel666'

import pygame
import os
from load_graphic_sound import *
from main_menu import *


class GameBackground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('background.jpg')
        self.rect.x = 0
        self.rect.y = 0

    def show_backgroud(self):
        background = GameBackground()
        background_sprite = pygame.sprite.Group(background)
        background_sprite.update()
        background_sprite.draw(screen)


# MAIN GAME
######################################################################
######################################################################
######################################################################

class Game(object):
    def main(self, screen_resolution):

        # GAME INITIALIZATION
        running = True
        clock = pygame.time.Clock()
        main_menu = MainMenu()

        background_image = GameBackground()
        while running is True:

            clock.tick(50)

            # STATE OF THE GAME

            show_main_menu = True
            saves_present = True
            main_menu.visible = True

            # GAME LOGIC

            # INPUT
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and pygame.K_ESCAPE:
                    return
                if event.type == pygame.MOUSEBUTTONUP and \
                        event.button == 1 and \
                        main_menu.quit_button.rect.collidepoint(pygame.mouse.get_pos()):
                    main_menu.visible = False
                    running = False

            # DISPLAYING
            background_image.show_backgroud()
            main_menu.show_menu(screen)

            pygame.display.flip()
            # SOUND AND MUSIC

##############################################################################

if __name__ == "__main__":
    pygame.init()
    # WINDOW SIZE
    screen_x = 1280
    screen_y = 720
    screen = pygame.display.set_mode((screen_x, screen_y))
    # FULLSCREEN
    # screen = pygame.display.set_mode((screen_x, screen_y), pygame.FULLSCREEN)
    Game().main(screen)