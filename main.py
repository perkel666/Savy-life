__author__ = 'perkel666'

import pygame
import os
from load_graphic_sound import load_image
from main_menu import *
from gameplay_menu import GameplayMenu
from options_menu import OptionsMenu
from player_creation_menu import *


# MAIN GAME
######################################################################
######################################################################
######################################################################

class Game(object):
    def __init__(self):
        # DEBUG
        self.debug = True
        # GAME INITIALIZATION
        self.running = True
        # INPUT INITIALIZATION
        self.clock = pygame.time.Clock()
        self.events = None
        self.mouse_position = None
        self.input_control = "main_menu"  # Current menu  OLD
        self.update_input_control = None
        # DOES PLAYER USED NEW GAME ?
        self.new_game_started = False

        # PLAYER LOCAL
        self.player = None

        ############ OLD
        self.player_creation_menu_visible = False
        self.main_menu_visible = True
        self.gameplay_menu_visible = False
        self.options_menu_visible = False                # REWORK
        self.load_menu_visible = False
        self.save_menu_visible = False
        ############ OLD

        # MENU INITIALIZATION
        self.menu_gameplay = GameplayMenu()
        self.menu_main = MainMenu()
        self.menu_options = OptionsMenu()
        self.menu_player_creation = PlayerCreationMenu()

        ########### OLD
        # player creation
        self.player = Player()
        ########## OLD

    def main(self, screen):
        # MAIN LOOP
        while self.running is True:
            self.clock.tick(60)
            self.events = pygame.event.get()
            self.mouse_position = pygame.mouse.get_pos()

            # DEBUG QUICK QUIT FROM GAME

            #
            if game.debug is True:
                for event in self.events:
                    # CLOSE PROGRAM VIA WINDOW CLOSE or ALT+F4
                    if event.type == pygame.QUIT:
                        game.running = False
                    # ESCAPE KEY
                    if event.type == pygame.KEYDOWN and pygame.K_ESCAPE:
                        game.running = False

            # DISPLAYING MENU LAYERS
            self.menu_gameplay.show_menu(screen, game)
            self.menu_main.show_menu(screen, game)
            self.menu_player_creation.show_menu(screen, game)
            self.menu_options.show_menu(screen, game)
            # FLIP BUFFER
            #pygame.display.flip()  # Updates whole screen
            pygame.display.update()  # Updates only changes between last and this frame

            # OUTPUT
            if self.update_input_control is not None:
                self.input_control = self.update_input_control
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