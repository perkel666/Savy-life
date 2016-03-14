__author__ = 'perkel666'

import os
import pygame
from load_graphic_sound import load_image
from sprite_effects import sprite_hover
from player_creation_menu import Player


class MainMenu():
    def __init__(self):
        self.visible = True
        self.input_control = True
        # MainMenu position
        self.position_x = 50
        self.position_y = 50
        # Buttons position relative to background position
        self.buttons_pos_x = 25
        self.buttons_pos_y = 40
        # Background image
        self.background = MainMenuBackground()
        self.background.rect.x = self.position_x
        self.background.rect.y = self.position_y
        # Background transparency
        self.transparency = MainMenuTransparency()
        # Buttons
        self.continue_button = ContinueButton()
        self.newgame_button = NewGameButton()
        self.save_button = SaveButton()
        self.load_button = LoadButton()
        self.option_button = OptionsButton()
        self.quit_button = QuitButton()
        # MainMenu background image layer
        self.mm_background = pygame.sprite.Group(self.background)
        # MainMenu transparency layer
        self.mm_transparency = pygame.sprite.Group(self.transparency)

    def show_menu(self, screen, game, events):
        if game.main_menu_visible is True:

            # MENU LOGIC
            # 1. Creating list of menu options

            menu_options = [
                self.continue_button,
                self.newgame_button,
                self.save_button,
                self.load_button,
                self.option_button,
                self.quit_button
            ]
            # 2. Creating list of visible menu options according to self.visible in button

            menu_options_active = []

            for menu_option in menu_options:
                if menu_option.visible is True:
                    menu_options_active.append(menu_option)

            # 3. Creating Buttons sprite group from menu_options_active and adding it to button layer

            mm_buttons = pygame.sprite.Group()
            buttons_starting_position_y = 75
            for button in menu_options_active:
                # placement
                button.rect.y = (self.position_y - self.buttons_pos_y) + buttons_starting_position_y
                button.rect.x = self.position_x + self.buttons_pos_x
                # checks for mouse hove and if True then it changes
                # button image for _hover version
                sprite_hover(button)

                mm_buttons.add(button)
                buttons_starting_position_y += 75
            # INPUT

            if game.input_control is "main_menu":
                for event in events:

                    # BUTTON CONTINUE
                    if event.type == pygame.MOUSEBUTTONUP and \
                            event.button == 1 and \
                            self.continue_button.rect.collidepoint(pygame.mouse.get_pos()):
                        game.main_menu_visible = False
                        game.gameplay_menu_visible = True
                        game.input_control = "gameplay_menu"
                        print "continue"

                    # BUTTON NEW GAME
                    if event.type == pygame.MOUSEBUTTONUP and \
                            event.button == 1 and \
                            self.newgame_button.rect.collidepoint(pygame.mouse.get_pos()):
                        game.main_menu_visible = False
                        game.player_creation_menu_visible = True
                        game.gameplay_menu_visible = False
                        self.continue_button.visible = True
                        game.new_game_started = True
                        game.input_control = "player_creation_menu"
                        print "new game"

                    # BUTTON OPTIONS
                    if event.type == pygame.MOUSEBUTTONUP and \
                            event.button == 1 and \
                            self.option_button.rect.collidepoint(pygame.mouse.get_pos()):

                        game.main_menu_visible = False
                        game.options_menu_visible = True
                        game.input_control = "options_menu"
                        print "options"

                    # BUTTON QUIT
                    if event.type == pygame.MOUSEBUTTONUP and \
                            event.button == 1 and \
                            self.quit_button.rect.collidepoint(pygame.mouse.get_pos()):
                        game.main_menu = False
                        game.running = False
                        print "quit"

            # UPDATE MENU GRAPHIC

            self.mm_transparency.update()
            self.mm_background.update()
            mm_buttons.update()

            # DISPLAY
            self.mm_transparency.draw(screen)
            self.mm_background.draw(screen)
            mm_buttons.draw(screen)
        else:
            pass


class MainMenuTransparency(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('menu_transparency.png')


class MainMenuBackground(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('mainmenubackground.png')


class ContinueButton(pygame.sprite.Sprite):
    def __init__(self):
        # TEMPLATE
        pygame.sprite.Sprite.__init__(self)
        # LOAD IMAGES AND SET RECTANGLE FOR SPRITE
        self.image, self.rect = load_image('continue_normal.png')
        self.image_hover, self.rect = load_image('continue_hover.png')
        self.image_no_hover = self.image
        # IS OPTION VISIBLE IN MENU
        self.visible = False
        # ORDER OF OPTION IN MENU
        self.order = 1
        # METHODS


class NewGameButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('newgame_normal.png')
        self.image_hover, self.rect = load_image('newgame_hover.png')
        self.image_no_hover = self.image
        self.visible = True
        self.order = 2


class SaveButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('save_normal.png')
        self.image_hover, self.rect = load_image('save_hover.png')
        self.image_no_hover = self.image
        self.visible = True
        self.order = 3


class LoadButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('load_normal.png')
        self.image_hover, self.rect = load_image('load_hover.png')
        self.image_no_hover = self.image
        self.visible = True
        self.order = 4


class OptionsButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('options_normal.png')
        self.image_hover, self.rect = load_image('options_hover.png')
        self.image_no_hover = self.image
        self.visible = True
        self.order = 5


class QuitButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('quit_normal.png')
        self.image_hover, self.rect = load_image('quit_hover.png')
        self.image_no_hover = self.image
        self.visible = True
        self.order = 6

