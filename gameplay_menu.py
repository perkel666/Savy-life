__author__ = 'perkel666'

import pygame
from load_graphic_sound import load_image
from load_graphic_sound import load_sprite


class GameplayMenu():
    def __init__(self):
        self.visible = False
        self.input_control = False
        # UI ELEMENTS
        self.text_box = TextBox()
        self.gameplay_background = load_sprite('gameplay_background.png')
        ##### UI ELEMENTS POSITION
        # Down bar
        self.down_bar_y = 525
        self.down_bar_x = 10

        # player portrait position
        self.player_portrait_position = (self.down_bar_x+10, self.down_bar_y+10)
        # text_box position
        self.text_box.rect.x = self.down_bar_x + 290
        self.text_box.rect.y = self.down_bar_y
        self.text_box_position = (self.down_bar_x+290, self.down_bar_y)

    def show_menu(self, screen, game, events):
        if game.gameplay_menu_visible is True:
            # MENU LOGIC
            # 1. Creating list of ui options
            ui_elements_list_front = [
                self.text_box
            ]
            # 2. Creating list of visible menu options according to self.visible in button

            ui_elements_visible_list_front = []
            for ui_element in ui_elements_list_front:
                if ui_element.visible is True:
                    ui_elements_visible_list_front.append(ui_element)
            # 3. Creating Buttons sprite group from menu_options_active and adding it to button layer

            ui_elements_front = pygame.sprite.Group()
            for ui_element in ui_elements_visible_list_front:
                ui_elements_front.add(ui_element)

            # 4. Background spriteGroup
            background = pygame.sprite.Group()
            background.add(self.gameplay_background)

            # INPUT
            if game.input_control is "gameplay_menu":
                for event in events:
                    if event.type == pygame.MOUSEBUTTONUP and \
                            event.button == 1 and \
                            game.player.player_background.rect.collidepoint(pygame.mouse.get_pos()):
                        game.main_menu_visible = True
                        game.gameplay_menu_visible = True
                        game.input_control = "main_menu"
                        print "show main menu"
            # UPDATE GRAPHIC
            background.update()
            ui_elements_front.update()
            # DISPLAY
            background.draw(screen)
            #ui_elements_front.draw(screen)
            game.player.show_player_portrait(self.player_portrait_position, screen)
            self.text_box.show_text_box(self.text_box_position, screen)


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