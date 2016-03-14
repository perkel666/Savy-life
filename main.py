__author__ = 'perkel666'

import pygame
import os
from load_graphic_sound import load_image
from main_menu import *
from gameplay_menu import GameplayMenu
from options_menu import OptionsMenu
from player_creation_menu import *


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
        # Event log
        self.events = None
        self.mouse_position = None
        self.new_game_started = False
        self.player_creation_menu_visible = False
        self.main_menu_visible = True
        self.gameplay_menu_visible = False
        self.options_menu_visible = False
        self.load_menu_visible = False
        self.save_menu_visible = False
        self.input_control = "main_menu"
        self.debug = False
        # BACKGROUND
        self.background_image = GameBackground()
        # player creation
        self.player = Player()

    def main(self, screen_resolution):

        # GAME INITIALIZATION
        clock = pygame.time.Clock()
        gameplay_menu = GameplayMenu()
        main_menu = MainMenu()
        options = OptionsMenu()
        player_creation_menu = PlayerCreationMenu(game)

        while self.running is True:

            clock.tick(60)
            self.events = pygame.event.get()
            self.mouse_position = pygame.mouse.get_pos()

            # STATE OF THE GAME

            # GAME LOGIC

            # INPUT

            for event in self.events:
                if event.type == pygame.QUIT:
                    game.running = False
                if event.type == pygame.KEYDOWN and pygame.K_ESCAPE:
                    game.running = False

            # DISPLAY background
            background_image = pygame.sprite.Group(self.background_image)
            background_image.update()
            background_image.draw(screen)

            # DISPLAYING
            gameplay_menu.show_menu(screen, game)
            main_menu.show_menu(screen, game)
            player_creation_menu.show_menu(screen, game)
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