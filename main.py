from __future__ import division

__author__ = 'perkel666'

from scripts.main_menu import *
from scripts.gameplay_menu import GameplayMenu
from scripts.options_menu import OptionsMenu
from scripts.player_creation_menu import *
from scripts.load_graphic_sound import *
from scripts.data_file_handling import FileList

files_list = FileList()


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
        self.fullscreen = None
        # DELTA TIME
        self.dt_seconds = None
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

            dt = self.clock.tick(120)
            self.dt_seconds = dt/1000
            self.mouse_position = pygame.mouse.get_pos()
            self.events = pygame.event.get()

            # DEBUG QUICK QUIT FROM GAME
            if self.debug is True:
                for event in self.events:
                    # Close via WINDOW CLOSE or ALT+F4
                    if event.type == pygame.QUIT:
                        self.running = False
                    # Close via ESCAPE KEY
                    if event.type == pygame.KEYDOWN and pygame.K_ESCAPE:
                        self.running = False

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

            # Switch game res
            if self.fullscreen is not None:
                if self.fullscreen is True:
                    pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
                    self.fullscreen = None
                elif self.fullscreen is False:
                    pygame.display.set_mode((1280, 720))
                    self.fullscreen = None


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