__author__ = 'perkel666'

import pygame
from load_graphic_sound import *


class GameplayMenu():
    def __init__(self):
        self.visible = False
        self.input_control = False

        # UI POSITIONING
        self.ui_position_bar_down = (10, 525)
        self.ui_position_text_box = (self.ui_position_bar_down[0]+290, self.ui_position_bar_down[1])
        self.ui_position_player_portrait = (self.ui_position_bar_down[0]+10, self.ui_position_bar_down[1]+10)

        # UI INITIALIZATION
        self.ui_background = GameplayMenu.UiBackground('gameplay_background.png')
        self.ui_text_box = GameplayMenu.UiTextBox('text_box.png')
        # self.ui_portrait_player = later i will move portrait here for now it is in game.player....

    def show_menu(self, screen, game):
        if game.gameplay_menu_visible is True:

            # LOCALS

            layer_background = pygame.sprite.Group()
            layer_gameplay_background = pygame.sprite.Group()
            layer_gameplay_layer_0 = pygame.sprite.Group()
            layer_gameplay_layer_1 = pygame.sprite.Group()
            layer_gameplay_layer_2 = pygame.sprite.Group()
            layer_gameplay_layer_3 = pygame.sprite.Group()
            layer_bar_down_background = pygame.sprite.Group()
            layer_bar_down_bottom = pygame.sprite.Group()
            layer_bar_down_top = pygame.sprite.Group()

            # POSITIONING UI

            game.player.player_background.rect.x,\
                game.player.player_background.rect.y = self.ui_position_player_portrait

            game.player.player_portrait.rect.x, \
                game.player.player_portrait.rect.y = self.ui_position_player_portrait

            self.ui_text_box.rect.x, self.ui_text_box.rect.y = self.ui_position_text_box

            # ADD SPRITES TO LAYERS

            layer_background = pygame.sprite.Group(self.ui_background)
            layer_bar_down_bottom = pygame.sprite.Group(game.player.player_background)
            layer_bar_down_top = pygame.sprite.Group(
                self.ui_text_box,
                game.player.player_portrait
            )

            if game.input_control is "gameplay_menu":
                game.player.player_background.get_state(game)

            if game.input_control is "gameplay_menu":
                game.player.player_background.do_action(game)

            # UPDATE SPRITE LAYERS

            layer_background.update()
            layer_gameplay_background.update()
            layer_gameplay_layer_0.update()
            layer_gameplay_layer_1.update()
            layer_gameplay_layer_2.update()
            layer_gameplay_layer_3.update()
            layer_bar_down_background.update()
            layer_bar_down_bottom.update()
            layer_bar_down_top.update()

            # DISPLAY

            layer_background.draw(screen)
            layer_gameplay_background.draw(screen)
            layer_gameplay_layer_0.draw(screen)
            layer_gameplay_layer_1.draw(screen)
            layer_gameplay_layer_2.draw(screen)
            layer_gameplay_layer_3.draw(screen)
            layer_bar_down_background.draw(screen)
            layer_bar_down_bottom.draw(screen)
            layer_bar_down_top.draw(screen)

    ##################################
    # CLASSES used in GameplayMenu() #
    ##################################

    class UiPlayerPortrait(CreateSprite2):
        def __init__(self, name):
            super(GameplayMenu.UiPlayerPortrait, self).__init__(name)
            self.description = "Player portrait"

        def do_action(self, game):
            if self.last_pressed is True:
                self.last_pressed = False

    class UiTextBox(CreateSprite2):
        def __init__(self, name):
            super(GameplayMenu.UiTextBox, self).__init__(name)
            self.description = "Text box"

        def do_action(self, game):
            if self.last_pressed is True:
                self.last_pressed = False

    class UiBackground(CreateSprite2):
        def __init__(self, name):
            super(GameplayMenu.UiBackground, self).__init__(name)
            self.description = "Background"

        def do_action(self, game):
            if self.last_pressed is True:
                self.last_pressed = False

#################################################################           OLD


class PlayerPortrait(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('player-001.png')
        self.visible = True


class TextBox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('text_box.png')
        self.background = load_sprite('text_box.png')
        self.visible = True
        self.current_text = "Random text SOMETHING BIG I THINK"

    def show_text_box(self, (x_pos, y_pos), screen):
        self.background.rect.x = x_pos
        self.background.rect.y = y_pos
        text_position_x = x_pos+5
        text_position_y = y_pos+5
        sprite = pygame.sprite.Group(self.background)
        sprite.update()
        sprite.draw(screen)


class GameplayScreen(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('gameplay_screen')
        self.visible = True

###############################################################                 OLD