__author__ = 'perkel666'

import os
import pygame
from load_graphic_sound import *
from sprite_effects import sprite_hover
from player_creation_menu import Player


class MainMenu():
    def __init__(self):
        self.visible = True
        self.input_control = True

        # UI POSITIONING
        self.position_menu = (50, 50)
        self.position_buttons = (self.position_menu[0]+25, self.position_menu[1]+40)
        self.difference_y_between_buttons = 75

        # MENU GRAPHIC
        self.main_menu_transparency = MainMenu.BackgroundTransparent('menu_transparency.png')
        self.main_menu_background = MainMenu.MenuBackground('background.jpg')
        self.main_menu_graphic = MainMenu.MainMenuUI('mainmenubackground.png', self.position_menu)

        self.menu_background_list = [
            self.main_menu_transparency,
            self.main_menu_background]

        # BUTTONS
        self.button_continue = MainMenu.ButtonContinue('main_menu_continue.png')
        self.button_new_game = MainMenu.ButtonNewGame('main_menu_new_game.png')
        self.button_save = MainMenu.ButtonSave('main_menu_save.png')
        self.button_load = MainMenu.ButtonLoad('main_menu_load.png')
        self.button_options = MainMenu.ButtonOptions('main_menu_options.png')
        self.button_quit = MainMenu.ButtonsQuit('main_menu_quit.png')

        self.menu_button_list = [
            self.button_continue,
            self.button_new_game,
            self.button_save,
            self.button_load,
            self.button_options,
            self.button_quit]

    def show_menu(self, screen, game):
        if game.main_menu_visible is True:
            # LOCALS
            menu_background_visible_list = []
            menu_buttons_visible_list = []

            layer_main_menu_buttons = pygame.sprite.Group()
            layer_main_menu_background = pygame.sprite.Group()
            layer_main_menu_ui_graphic = pygame.sprite.Group()

            # CREATING VISIBLE BUTTONS LIST
            for button in self.menu_button_list:
                if button.visible is True:
                    menu_buttons_visible_list.append(button)

            # CREATING VISIBLE BACKGROUND LIST (depends on: if game.new_game_started is True or False)
            for background in self.menu_background_list:
                if background.visible is True:
                    menu_background_visible_list.append(background)

            # POSITIONING BUTTONS ON MAIN MENU
            difference = 0  # initial difference
            for button in menu_buttons_visible_list:
                button.rect.x = self.position_buttons[0]
                button.rect.y = self.position_buttons[1] + difference
                difference += self.difference_y_between_buttons

            # INPUT
            # CHANGING GRAPHICAL STATE ADDING TO SPRITE GROUP AND RECEIVING INPUT
            if game.input_control is "main_menu":
                for button in menu_buttons_visible_list:
                    button.get_state(game)

            # OUTPUT
            # EXECUTING BUTTON IF IT WAS PRESSED
            if game.input_control is "main_menu":
                for button in menu_buttons_visible_list:
                    button.do_action(game)

            # ADD SPRITES TO LAYERS
            for background in menu_background_visible_list:
                layer_main_menu_background.add(background)

            for button in menu_buttons_visible_list:
                layer_main_menu_buttons.add(button)

            if self.main_menu_graphic.visible is True:
                layer_main_menu_ui_graphic.add(self.main_menu_graphic)

            # UPDATE LAYERS
            layer_main_menu_background.update()
            layer_main_menu_ui_graphic.update()
            layer_main_menu_buttons.update()

            # DISPLAY LAYERS
            layer_main_menu_background.draw(screen)
            layer_main_menu_ui_graphic.draw(screen)
            layer_main_menu_buttons.draw(screen)

    ##############################
    # CLASSES used in MainMenu() #
    ##############################

    # BACKGROUND ##################################
    # TRANSPARENT BACKGROUND ONCE YOU START NEWGAME
    class BackgroundTransparent(CreateSprite2):
        def __init__(self, name):
            super(MainMenu.BackgroundTransparent, self).__init__(name)
            self.description = "Background transparency"
            self.visible = True

    # MAIN MENU BACKGROUND IMAGE BEFORE START OF GAME-PLAY
    class MenuBackground(CreateSprite2):
        def __init__(self, name):
            super(MainMenu.MenuBackground, self).__init__(name)
            self.description = "Background image"
            self.visible = True

    # MAIN MENU UI GRAPHIC
    class MainMenuUI(CreateSprite2):
        def __init__(self, name,  position_tuple_x_y):
            super(MainMenu.MainMenuUI, self).__init__(name)
            self.description = "Main menu UI"
            self.rect.x = position_tuple_x_y[0]
            self.rect.y = position_tuple_x_y[1]
            self.visible = True

    # BUTTONS #########
    # BUTTON - CONTINUE
    class ButtonContinue(CreateSprite2):
        def __init__(self, name):
            super(MainMenu.ButtonContinue, self).__init__(name, hover=True)
            self.description = "Continue game"
            self.order = 1
            self.visible = False

        def do_action(self, game):
            if self.last_pressed is True:
                game.main_menu_visible = False
                game.gameplay_menu_visible = True
                game.input_control = "gameplay_menu"
                print "continue"
                self.last_pressed = False

    # BUTTON - NEW GAME
    class ButtonNewGame(CreateSprite2):
        def __init__(self, name):
            super(MainMenu.ButtonNewGame, self).__init__(name, hover=True)
            self.description = "Start new game"
            self.order = 2

        def do_action(self, game):
            if self.last_pressed is True:
                game.main_menu_visible = False
                game.player_creation_menu_visible = True
                game.gameplay_menu_visible = False
                game.menu_main.button_continue.visible = True
                game.new_game_started = True
                game.input_control = "player_creation_menu"
                print "new game"
                self.last_pressed = False

    # BUTTON - SAVE
    class ButtonSave(CreateSprite2):
        def __init__(self, name):
            super(MainMenu.ButtonSave, self).__init__(name, hover=True)
            self.description = "Save progress"
            self.order = 3

        def do_action(self, game):
            if self.last_pressed is True:
                self.last_pressed = False

    # BUTTON - LOAD
    class ButtonLoad(CreateSprite2):
        def __init__(self, name):
            super(MainMenu.ButtonLoad, self).__init__(name, hover=True)
            self.description = "Load progress"
            self.order = 4

        def do_action(self, game):
            if self.last_pressed is True:
                self.last_pressed = False

    # BUTTON - OPTIONS
    class ButtonOptions(CreateSprite2):
        def __init__(self, name):
            super(MainMenu.ButtonOptions, self).__init__(name, hover=True)
            self.description = "Configure options"
            self.order = 5

        def do_action(self, game):
            if self.last_pressed is True:
                game.main_menu_visible = False
                game.options_menu_visible = True
                game.input_control = "options_menu"
                print "options"
                self.last_pressed = False

    # BUTTON - QUIT
    class ButtonsQuit(CreateSprite2):
        def __init__(self, name):
            super(MainMenu.ButtonsQuit, self).__init__(name, hover=True)
            self.description = "Quit"
            self.order = 6

        def do_action(self, game):
            if self.last_pressed is True:
                game.main_menu_visible = False
                print "quit"
                game.running = False
                self.last_pressed = False