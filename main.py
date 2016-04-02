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

        # MENU INITIALIZATION
        self.menu_gameplay = GameplayMenu()
        self.menu_main = MainMenu()
        self.menu_options = OptionsMenu()
        self.menu_player_creation = PlayerCreationMenu()

        self.main_menu_list = [
            self.menu_gameplay,
            self.menu_player_creation,
            self.menu_main,
            self.menu_options
        ]

        ########### OLD
        # player creation
        self.player = Player()
        ########## OLD

    def main_loop(self):
        while self.running is True:
            self.start_frame()
            self.get_input()
            self.get_events()
            self.display()
            self.handle_events()

    def start_frame(self):
        """
        Initialization of basic lists, clock tick rate, calculating delta time,
        getting pygame kayboard/mouse events,
        cleaning up custom events list
        """

        dt = self.clock.tick(120)
        self.dt_seconds = dt/1000
        self.mouse_position = pygame.mouse.get_pos()
        self.events = pygame.event.get()
        self.game_events = []
        self.key_mouse_event_list = []

    def get_input(self):
        self.gi_debug()
        self.gi_mouse()
        self.gi_keys()

    def get_events(self):
        pass

    def handle_events(self):

        self.check_system_events()
        self.main_menu_events()

    def display(self):

        # GAMEPLAY

        # GAMEPLAY UI

        # MAIN UI
        self.di_menu()
        # DRAW
        pygame.display.update()

    def di_menu(self):
        self.menu_gameplay.show_menu(screen, game)
        self.menu_main.show_menu(screen, game)
        self.menu_player_creation.show_menu(screen, game)
        self.menu_options.show_menu(screen, game)

    def gi_debug(self):
        for event in self.events:
            # Close via WINDOW CLOSE
            if event.type == pygame.QUIT:
                self.game_events.append('SYSTEM:QUIT')
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print "ESCAPE"
                    self.key_mouse_event_list.append('K_ESCAPE')
                if event.key == pygame.K_SPACE:
                    print "SPACE"
                    self.key_mouse_event_list.append('K_SPACE')
                if event.key == pygame.K_LALT:
                    print 'LEFT ALT'
                    self.key_mouse_event_list.append('K_LALT')
                if event.key == pygame.K_F4:
                    print 'F4'
                    self.key_mouse_event_list.append('K_F4')

    def gi_mouse(self):
        for event in self.events:
            # mouse left click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.key_mouse_event_list.append('lmb_down')
                print "lmb"
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.key_mouse_event_list.append('lmb_up')
            # mouse right click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                self.key_mouse_event_list.append('rmb_down')
                print "rmb"
            if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                self.key_mouse_event_list.append('rmb_up')
            # mouse middle click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
                self.key_mouse_event_list.append('mmb_down')
                print "mmb"
            if event.type == pygame.MOUSEBUTTONUP and event.button == 2:
                self.key_mouse_event_list.append('mmb_up')
            # mouse scroll up
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                self.key_mouse_event_list.append('mmb_down')
                print "scroll up"
            if event.type == pygame.MOUSEBUTTONUP and event.button == 4:
                self.key_mouse_event_list.append('mmb_up')
            # mouse scroll down
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                self.key_mouse_event_list.append('mmb_down')
                print "scroll down"
            if event.type == pygame.MOUSEBUTTONUP and event.button == 5:
                self.key_mouse_event_list.append('mmb_up')

    def gi_keys(self):
        """
        for event in self.events:
            if event.type == pygame.KEYDOWN and pygame.K_SPACE:
                self.key_mouse_event_list.append('k_space_down')
                print 'k_space_down'
            if event.type == pygame.KEYUP and pygame.K_SPACE:
                self.key_mouse_event_list.append('k_space_up')
                print 'k_space_up'
        """

    def check_system_events(self):

        for event in self.game_events:
            if event == 'SYSTEM:QUIT':
                self.running = False
            elif event == 'SYSTEM:FULLSCREEN':
                pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
                print "changing to Fullscreen"
            elif event == 'SYSTEM:WINDOWED':
                pygame.display.set_mode((1280, 720))
                print "changing to windowed"

    def main_menu_events(self):

        if self.update_input_control is not None:
            self.input_control = self.update_input_control


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
    #game.main(screen)
    game.main_loop()