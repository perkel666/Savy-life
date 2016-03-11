__author__ = 'perkel666'

import pygame
from load_graphic_sound import load_image
from load_graphic_sound import load_sprite
from debug import debug


class GameplayMenu():
    def __init__(self):
        self.visible = False
        self.input_control = False
        # UI ELEMENTS
        self.player_portrait = PlayerPortrait()
        self.text_box = TextBox()
        ##### UI ELEMENTS POSITION
        # Down bar
        self.down_bar_y = 525
        self.down_bar_x = 10
        self.player_portrait.rect.x = self.down_bar_x + 10
        self.player_portrait.rect.y = self.down_bar_y
        self.text_box.rect.x = self.down_bar_x + 290
        self.text_box.rect.y = self.down_bar_y

    def show_menu(self, screen, game):
        if game.gameplay_menu_visible is True:
            # MENU LOGIC
            # 1. Creating list of menu options

            ui_elements_list = [
                self.player_portrait,
                self.text_box
            ]
            debug("ui_elements_list creation", game)
            # 2. Creating list of visible menu options according to self.visible in button

            ui_elements_visible_list = []

            for ui_element in ui_elements_list:
                if ui_element.visible is True:
                    ui_elements_visible_list.append(ui_element)
            debug("ui_elements_visible list", game)
            # 3. Creating Buttons sprite group from menu_options_active and adding it to button layer

            ui_elements = pygame.sprite.Group()
            for ui_element in ui_elements_visible_list:
                ui_elements.add(ui_element)
            debug("ui_elements sprite group creation", game)

            # INPUT
            if game.input_control == "gameplay_menu":
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP and \
                            event.button == 1 and \
                            self.player_portrait.rect.collidepoint(pygame.mouse.get_pos()):
                        game.main_menu_visible = True
                        game.gameplay_menu_visible = True
                        game.input_control = "main_menu"
                        print "show main menu"
            # UPDATE GRAPHIC
            ui_elements.update()
            # DISPLAY
            ui_elements.draw(screen)
            debug("draw screen", game)


class PlayerPortrait(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('player.png')
        self.visible = True


class TextBox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('text_box.png')
        self.visible = True


class GameplayScreen(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('gameplay_screen')
        self.visible = True