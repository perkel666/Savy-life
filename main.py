__author__ = 'perkel666'

import pygame
import os
from load_graphic_sound import *
from main_menu import *
from gameplay_menu import GameplayMenu


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
    def __init__(self):
        self.running = True
        self.main_menu_visible = True
        self.gameplay_menu_visible = False
        self.debug = False

    def main(self, screen_resolution):

        # GAME INITIALIZATION
        clock = pygame.time.Clock()
        gameplay_menu = GameplayMenu()
        main_menu = MainMenu()

        background_image = GameBackground()
        while self.running is True:

            clock.tick(30)

            # STATE OF THE GAME

            # GAME LOGIC

            # INPUT
            """
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and pygame.K_ESCAPE:
                    return
            """
            """
                if event.type == pygame.MOUSEBUTTONUP and \
                        event.button == 1 and \
                        main_menu.quit_button.rect.collidepoint(pygame.mouse.get_pos()):
                    main_menu.visible = False
                    self.running = False
            """

            # DISPLAYING
            background_image.show_backgroud()
            gameplay_menu.show_menu(screen, game)
            main_menu.show_menu(screen, game)


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
    game = Game()
    game.main(screen)