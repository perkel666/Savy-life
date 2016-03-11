__author__ = 'perkel666'

import pygame
from load_graphic_sound import load_image
from load_graphic_sound import load_sprite


class GameplayMenu():
    def __init__(self):
        self.visible = False
        self.input_control = False
        # UI ELEMENTS
        self.player_portrait_background = load_sprite('player_background_01.png')
        self.player_portrait = load_sprite('player.png')
        self.text_box = load_sprite('text_box.png')
        self.gameplay_background = load_sprite('gameplay_background.png')
        ##### UI ELEMENTS POSITION
        # Down bar
        self.down_bar_y = 525
        self.down_bar_x = 10
        # player portrait background
        self.player_portrait_background.rect.x = self.down_bar_x + 10
        self.player_portrait_background.rect.y = self.down_bar_y
        # player portrait position
        self.player_portrait.rect.x = self.player_portrait_background.rect.x
        self.player_portrait.rect.y = self.player_portrait_background.rect.y
        # text_box position
        self.text_box.rect.x = self.down_bar_x + 290
        self.text_box.rect.y = self.down_bar_y

    def show_menu(self, screen, game):
        if game.gameplay_menu_visible is True:
            # MENU LOGIC
            # 1. Creating list of ui options
            ui_elements_list_front = [
                self.player_portrait,
                self.text_box
            ]

            ui_elements_list_background = [
                self.player_portrait_background
            ]
            # 2. Creating list of visible menu options according to self.visible in button

            ui_elements_visible_list_front = []
            for ui_element in ui_elements_list_front:
                if ui_element.visible is True:
                    ui_elements_visible_list_front.append(ui_element)
            ui_elements_visible_list_background = []
            for ui_element in ui_elements_list_background:
                if ui_element.visible is True:
                    ui_elements_visible_list_background.append(ui_element)
            # 3. Creating Buttons sprite group from menu_options_active and adding it to button layer

            ui_elements_front = pygame.sprite.Group()
            for ui_element in ui_elements_visible_list_front:
                ui_elements_front.add(ui_element)

            ui_elements_background = pygame.sprite.Group()
            for ui_element in ui_elements_visible_list_background:
                ui_elements_background.add(ui_element)

            # 4. Background spriteGroup
            background = pygame.sprite.Group()
            background.add(self.gameplay_background)

            # INPUT
            if game.input_control is "gameplay_menu":
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP and \
                            event.button == 1 and \
                            self.player_portrait.rect.collidepoint(pygame.mouse.get_pos()):
                        game.main_menu_visible = True
                        game.gameplay_menu_visible = True
                        game.input_control = "main_menu"
                        print "show main menu"
            # UPDATE GRAPHIC
            background.update()
            ui_elements_background.update()
            ui_elements_front.update()
            # DISPLAY
            background.draw(screen)
            ui_elements_background.draw(screen)
            ui_elements_front.draw(screen)


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