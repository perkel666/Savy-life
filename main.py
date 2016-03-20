from __future__ import division

__author__ = 'perkel666'

from scripts.main_menu import *
from scripts.gameplay_menu import GameplayMenu
from scripts.options_menu import OptionsMenu
from scripts.player_creation_menu import *
from scripts.load_graphic_sound import *
from scripts.data_file_handling import FileList

# GLOBALS
files_list = FileList()


class Game(object):
    def __init__(self):
        self.debug = True
        self.running = True
        self.fullscreen = None
        self.dt_seconds = None
        self.clock = pygame.time.Clock()
        self.events = None
        self.mouse_position = None
        self.key_mouse_event_list = []
        self.game_events = []
        self.input_control = "main_menu"  # Current menu input handling OLD
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

    def main_loop(self):
        while self.running is True:
            self.start_frame()
            self.get_input()
            self.get_events()
            self.handle_events()
            self.display()

    def start_frame(self):
        """
        Initialization of basic lists, clock tick rate, calculating delta time,
        getting pygame kayboard/mouse events,
        cleaning up custom events list
        :return:
        """

        dt = self.clock.tick(120)
        self.dt_seconds = dt/1000
        self.mouse_position = pygame.mouse.get_pos()
        self.events = pygame.event.get()
        self.game_events = []
        self.key_mouse_event_list = []

    def get_input(self):
        for event in self.events:
            # Close via WINDOW CLOSE or ALT+F4
            if event.type == pygame.QUIT:
                self.running = False
                self.game_events.append('SYSTEM:QUIT')
            # Close via ESCAPE KEY
            if event.type == pygame.KEYDOWN and pygame.K_ESCAPE:
                self.running = False
                self.game_events.append('SYSTEM:QUIT')
            # mouse left click
            if event.type == pygame.MOUSEBUTTONDOWN and event.key == 1:
                self.key_mouse_event_list.append('lmb_down')
            if event.type == pygame.MOUSEBUTTONUP and event.key == 1:
                self.key_mouse_event_list.append('lmb_up')
            # mouse right click
            if event.type == pygame.MOUSEBUTTONDOWN and event.key == 3:
                self.key_mouse_event_list.append('rmb_down')
            if event.type == pygame.MOUSEBUTTONUP and event.key == 3:
                self.key_mouse_event_list.append('rmb_up')
            # mouse middle click
            if event.type == pygame.MOUSEBUTTONDOWN and event.key == 2:
                self.key_mouse_event_list.append('mmb_down')
            if event.type == pygame.MOUSEBUTTONUP and event.key == 2:
                self.key_mouse_event_list.append('mmb_up')
            # mouse scroll up
            if event.type == pygame.MOUSEBUTTONDOWN and event.key == 4:
                self.key_mouse_event_list.append('mmb_down')
            if event.type == pygame.MOUSEBUTTONUP and event.key == 4:
                self.key_mouse_event_list.append('mmb_up')
            # mouse scroll down
            if event.type == pygame.MOUSEBUTTONDOWN and event.key == 5:
                self.key_mouse_event_list.append('mmb_down')
            if event.type == pygame.MOUSEBUTTONUP and event.key == 5:
                self.key_mouse_event_list.append('mmb_up')
            # SPACE
            if event.type == pygame.KEYDOWN and pygame.K_SPACE:
                self.key_mouse_event_list.append('k_space_up')
            if event.type == pygame.KEYUP and pygame.K_SPACE:
                self.key_mouse_event_list.append('k_space_down')

    def get_events(self):
        pass

    def handle_events(self):

        self.check_system_events()

    def display(self):

        # GAMEPLAY
        # GAMEPLAY UI
        # MAIN UI
        self.menu_gameplay.show_menu(screen, game)
        self.menu_main.show_menu(screen, game)
        self.menu_player_creation.show_menu(screen, game)
        self.menu_options.show_menu(screen, game)
        # DISPLAY
        pygame.display.update()

    def check_system_events(self):

        for event in list(set(self.key_mouse_event_list)):
            if event == 'SYSTEM:QUIT':
                self.running = False
            if event == 'SYSTEM:FULLSCREEN':
                pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
            if event == 'SYSTEM:WINDOWED':
                pygame.display.set_mode((1280, 720))

    def main_menu_events(self):
        pass



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