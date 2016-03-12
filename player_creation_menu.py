__author__ = 'perkel666'
import pygame
from load_graphic_sound import *
from sprite_effects import *
import os


###
### PLAYER CLASS
###

class Player():
    def __init__(self):
        # Basic info
        self.name = "Enter Name"
        self.sex = "male"
        self.money = 0
        # Portrait
        self.player_portrait = load_sprite('player-001.png')
        self.player_background = load_sprite('player_background_001.png')
        # Base statistics
        self.strenght = 5
        self.endurance = 5
        self.agility = 5
        self.percepcion = 5
        self.inteligence = 5
        self.charisma = 5
        # health and stamina
        self.health = self.strenght*10 + self.endurance*10
        self.stamina = self.endurance*20
        # Skills
        # Traits
        # Backstory

    def show_player_portrait(self, x_axis, y_axis, screen):
        #POSITION OF PORTRAIT
        self.player_portrait.rect.x = x_axis
        self.player_portrait.rect.y = y_axis
        self.player_background.rect.x = x_axis
        self.player_background.rect.y = y_axis
        #CREATING LAYERS TO DISPLAY
        layer_background = pygame.sprite.Group(self.player_background)
        layer_face = pygame.sprite.Group(self.player_portrait)
        #UPDATE SPRITES
        layer_background.update()
        layer_face.update()
        #DISPLAY
        layer_background.draw(screen)
        layer_face.draw(screen)


class PlayerCreationMenu():
    def __init__(self, game):
        self.visible = False
        #Menu Background image
        self.background_image = load_sprite('player_creation_screen.png')
        self.background_image.rect.x = 0
        self.background_image.rect.y = 0
        # Buttons
        self.button_finish = FinishButton()
        self.button_finish.rect.x = 900
        self.button_finish.rect.y = 600
        # PC ARROWS
        self.button_ar_right = PcArrowRight()
        self.button_ar_right.rect.x = 655
        self.button_ar_right.rect.y = 160

        self.button_ar_left = PcArrowLeft()
        self.button_ar_left.rect.x = self.button_ar_right.rect.x - 150
        self.button_ar_left.rect.y = self.button_ar_right.rect.y

        # choose player head
        player_portrait_list = os.listdir('data/art/player/head')
        player_background_list = os.listdir('data/art/player/backgrounds')
        game.player.player_portrait = load_sprite(player_portrait_list[1])
        game.player.player_background = load_sprite(player_background_list[2])

    def show_menu(self, screen, game):
        if game.player_creation_menu_visible is True:
            #MENU LOGIC
            sprite_group_background = pygame.sprite.Group(self.background_image)
            sprite_hover(self.button_finish)
            sprite_pressed(self.button_ar_left)
            sprite_pressed(self.button_ar_right)
            sprite_group_buttons = pygame.sprite.Group(
                self.button_finish,
                self.button_ar_right,
                self.button_ar_left)
            #INPUT
            if game.input_control is "player_creation_menu":
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP and \
                            event.button == 1 and \
                            self.background_image.rect.collidepoint(pygame.mouse.get_pos()):
                        game.main_menu_visible = True
                        game.player_creation_menu_visible = False
                        game.input_control = "main_menu"
                        print "show main menu "
                    if event.type == pygame.MOUSEBUTTONUP and \
                            event.button == 1 and \
                            self.button_finish.rect.collidepoint(pygame.mouse.get_pos()):
                        game.main_menu_visible = False
                        game.player_creation_menu_visible = False
                        game.gameplay_menu_visible = True
                        game.input_control = "gameplay_menu"
                        print "show game-play screen"

            #UPDATE
            sprite_group_background.update()
            sprite_group_buttons.update()
            #DISPLAY
            sprite_group_background.draw(screen)
            game.player.show_player_portrait(
                self.background_image.rect.x+550,
                self.background_image.rect.y+130,
                screen)
            sprite_group_buttons.draw(screen)


class FinishButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('pc_button_finish.png')
        self.image_no_hover = self.image
        self.image_hover, self.rect = load_image('pc_button_finish_hover.png')


class PcArrowRight(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.pressed = False
        self.image, self.rect = load_image('pc_right_arrow_normal.png')
        self.image_no_hover = self.image
        self.image_hover, self.rect = load_image('pc_right_arrow_hover.png')
        self.image_pressed, self.rect = load_image('pc_right_arrow_pressed.png')


class PcArrowLeft(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('pc_left_arrow_normal.png')
        self.image_no_hover = self.image
        self.image_hover, self.rect = load_image('pc_left_arrow_hover.png')
        self.image_pressed, self.rect = load_image('pc_left_arrow_pressed.png')