__author__ = 'Perkel'

import pygame
from load_graphic_sound import *
from sprite_effects import sprite_hover


class OptionsMenu():
    def __init__(self):
        self.visible = False
        self.input_control = False
        # Transparency
        self.transparency = pygame.sprite.Group(load_sprite('menu_transparency.png'))
        # BACKGROUND
        self.options_menu_background = OptionsMenuBackground()
        self.options_menu_background.rect.x = 50
        self.options_menu_background.rect.y = 50
        # close button and position
        self.close_button = CloseButton()
        self.close_button.rect.x = self.options_menu_background.rect.x + 700
        self.close_button.rect.y = self.options_menu_background.rect.y + 50
        # Buttons
        self.buttons_position_x = self.options_menu_background.rect.x + 30
        self.buttons_position_y = self.options_menu_background.rect.y + 40
        self.button_game = ButtonGame()
        self.button_sound = ButtonSound()
        self.button_back = ButtonBack()
        self.button_display = ButtonDisplay()
        # List of buttons
        self.buttons_list = [
            self.button_game,
            self.button_display,
            self.button_sound,
            self.button_back
        ]
        # Buttons body
        self.options_body_main_background = OptionsBody()
        self.options_body_main_background.rect.x = self.options_menu_background.rect.x + 275
        self.options_body_main_background.rect.y = self.options_menu_background.rect.y + 40

    def show_menu(self, screen, game):
        if game.options_menu_visible is True:

            #
            # MENU LOGIC
            #

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

            # Buttons positioning and adding to sprite group.
            count = 0
            for button in self.buttons_list:
                button.rect.x = self.buttons_position_x
                button.rect.y = self.buttons_position_y + (count * 70)
                count += 1
            # Buttons adding to sprite group and changing art based on hover mouse
            buttons_layer = pygame.sprite.Group()

            for button in self.buttons_list:
                sprite_hover(button)
                buttons_layer.add(button)

            # display button body

            options_body_main = pygame.sprite.Group()
            for button in self.buttons_list:
                if button.selected is True:
                    options_body_main.add(self.options_body_main_background)

            #
            # INPUT
            #

            # check if mouse hovers over button and if clicked with left mouse button DO SOMETHING
            if game.input_control is "options_menu":
                for event in game.events:

                    # - CLOSE BUTTON (RIGHT CORNER)
                    if event.type == pygame.MOUSEBUTTONUP and \
                            event.button == 1 and \
                            self.close_button.rect.collidepoint(game.mouse_position):
                        game.main_menu_visible = True
                        game.options_menu_visible = False
                        game.input_control = "main_menu"
                        print "show main menu"

                    # GAME BUTTON
                    if event.type == pygame.MOUSEBUTTONUP and \
                            event.button == 1 and \
                            self.button_game.rect.collidepoint(game.mouse_position):
                        self.button_game.selected = True
                        self.button_display.selected = False
                        self.button_sound.selected = False
                        print "button_game"

                    # DISPLAY BUTTON
                    if event.type == pygame.MOUSEBUTTONUP and \
                            event.button == 1 and \
                            self.button_display.rect.collidepoint(game.mouse_position):
                        self.button_game.selected = False
                        self.button_display.selected = True
                        self.button_sound.selected = False
                        print "button_display"

                    # SOUND BUTTON
                    if event.type == pygame.MOUSEBUTTONUP and \
                            event.button == 1 and \
                            self.button_sound.rect.collidepoint(game.mouse_position):
                        self.button_game.selected = False
                        self.button_display.selected = False
                        self.button_sound.selected = True
                        print "button_sound"

                    # BACK BUTTON
                    if event.type == pygame.MOUSEBUTTONUP and \
                            event.button == 1 and \
                            self.button_back.rect.collidepoint(game.mouse_position):
                        game.main_menu_visible = True
                        game.options_menu_visible = False
                        self.button_game.selected = False
                        self.button_display.selected = False
                        self.button_sound.selected = False
                        game.input_control = "main_menu"
                        print "button_back"

            # UPDATE GRAPHIC
            self.transparency.update()
            background.update()
            options_body_main.update()
            buttons_layer.update()
            buttons_sprite_layer.update()
            # DISPLAY
            self.transparency.draw(screen)
            background.draw(screen)
            options_body_main.draw(screen)
            buttons_layer.draw(screen)
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

### BUTTONS


class ButtonDisplay(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('button_display.png')
        self.image_no_hover = self.image
        self.image_hover, self.rect = load_image('button_display_hover.png')
        self.selected = False


class ButtonSound(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('button_sound.png')
        self.image_no_hover = self.image
        self.image_hover, self.rect = load_image('button_sound_hover.png')
        self.selected = False


class ButtonGame(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('button_game.png')
        self.image_no_hover = self.image
        self.image_hover, self.rect = load_image('button_game_hover.png')
        self.selected = False


class ButtonBack(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('button_back.png')
        self.image_no_hover = self.image
        self.image_hover, self.rect = load_image('button_back_hover.png')
        self.selected = False


class OptionsBody(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('options_menu_body.png')
        self.visible = False