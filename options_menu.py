__author__ = 'Perkel'

import pygame
from load_graphic_sound import load_image


class OptionsMenu():
    def __init__(self):
        self.visible = False

        # BACKGROUND
        self.options_menu_background = OptionsMenuBackground()
        self.options_menu_background.rect.x = 50
        self.options_menu_background.rect.y = 50

    def show_menu(self, screen, game):
        if game.options_menu_visible is True:

            # MENU LOGIC
            background = pygame.sprite.Group()
            background.add(self.options_menu_background)
            # INPUT
            if game.input_control == "options_menu":
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP and \
                            event.button == 1 and \
                            self.options_menu_background.rect.collidepoint(pygame.mouse.get_pos()):
                        game.main_menu_visible = True
                        game.gameplay_menu_visible = True
                        game.options_menu_visible = False
                        game.input_control = "main_menu"
                        print "show main menu"
            # UPDATE GRAPHIC
            background.update()
            # DISPLAY
            background.draw(screen)


class OptionsMenuBackground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('options_menu_background.png')
        self.visible = True
