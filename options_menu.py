__author__ = 'Perkel'

import pygame
from load_graphic_sound import load_image
from sprite_effects import sprite_hover


class OptionsMenu():
    def __init__(self):
        self.visible = False

        # BACKGROUND
        self.options_menu_background = OptionsMenuBackground()
        self.options_menu_background.rect.x = 50
        self.options_menu_background.rect.y = 50

        # close button and position
        self.close_button = CloseButton()
        self.close_button.rect.x = self.options_menu_background.rect.x + 700
        self.close_button.rect.x = self.options_menu_background.rect.y + 50

    def show_menu(self, screen, game):
        if game.options_menu_visible is True:

            # MENU LOGIC
            background = pygame.sprite.Group()
            background.add(self.options_menu_background)
            active_buttons = [
                self.close_button
            ]
            buttons_sprite_layer = pygame.sprite.Group()
            for button in active_buttons:
                if button.image_hover is not None:
                    sprite_hover(button)
                buttons_sprite_layer.add(button)
            # INPUT
            if game.input_control == "options_menu":
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP and \
                            event.button == 1 and \
                            self.close_button.rect.collidepoint(pygame.mouse.get_pos()):
                        game.main_menu_visible = True
                        game.gameplay_menu_visible = True
                        game.options_menu_visible = False
                        game.input_control = "main_menu"
                        print "show main menu"
            # UPDATE GRAPHIC
            background.update()
            buttons_sprite_layer.update()
            # DISPLAY
            background.draw(screen)
            buttons_sprite_layer.draw(screen)


class OptionsMenuBackground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('options_menu_background.png')
        self.visible = True


class CloseButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('close_options_normal.png')
        self.image_no_hover = self.image
        self.image_hover, self.rect = load_image('close_options_hover.png')

