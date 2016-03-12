__author__ = 'perkel666'

import pygame
import os
from load_graphic_sound import load_image
from main_menu import *
from gameplay_menu import GameplayMenu
from options_menu import OptionsMenu


class GameBackground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('background.jpg')


# MAIN GAME
######################################################################
######################################################################
######################################################################

class Game(object):
    def __init__(self):
        self.running = True
        self.new_game_started = False
        self.main_menu_visible = True
        self.gameplay_menu_visible = False
        self.options_menu_visible = False
        self.load_menu_visible = False
        self.save_menu_visible = False
        self.input_control = "main_menu"
        self.debug = False
        # BACKGROUND
        self.background_image = GameBackground()

    def main(self, screen_resolution):

        # GAME INITIALIZATION
        clock = pygame.time.Clock()
        gameplay_menu = GameplayMenu()
        main_menu = MainMenu()
        options = OptionsMenu()

        while self.running is True:

            clock.tick(60)

            # STATE OF THE GAME

            # GAME LOGIC

            # INPUT

            # DISPLAY background
            background_image = pygame.sprite.Group(self.background_image)
            background_image.update()
            background_image.draw(screen)

            # DISPLAYING
            gameplay_menu.show_menu(screen, game)
            main_menu.show_menu(screen, game)
            options.show_menu(screen, game)

            pygame.display.flip()
            # SOUND AND MUSIC


##############################################################################

if __name__ == "__main__":
    pygame.init()
    # Window decoration
    # icon = pygame.image.load('gameicon.png')
    # pygame.display.set_icon(icon)
    # pygame.display.set_caption('Main Window Tutorial')
    # WINDOW SIZE
    screen_x = 1280
    screen_y = 720
    screen = pygame.display.set_mode((screen_x, screen_y))
    # FULLSCREEN
    # screen = pygame.display.set_mode((screen_x, screen_y), pygame.FULLSCREEN)
    game = Game()
    game.main(screen)