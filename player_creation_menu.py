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
        self.player_portrait = Player.PlayerFace('player-001.png')
        self.player_background = Player.PlayerBackground('player_background_001.png')
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

    def show_player_portrait(self, (x_axis, y_axis), screen):
        #POSITION OF PORTRAIT
        face = self.player_portrait
        background = self.player_background

        face.rect.x = x_axis
        face.rect.y = y_axis
        background.rect.x = x_axis
        background.rect.y = y_axis
        #CREATING LAYERS TO DISPLAY
        layer_background = pygame.sprite.Group(background)
        layer_face = pygame.sprite.Group(face)
        #UPDATE SPRITES
        layer_background.update()
        layer_face.update()
        #DISPLAY
        layer_background.draw(screen)
        layer_face.draw(screen)

    class PlayerBackground(CreateSprite2):
        def __init__(self, name):
            super(Player.PlayerBackground, self).__init__(name)
            self.description = "Next background"

        def do_action(self, game):
            if self.last_pressed is True:
                game.main_menu_visible = True
                game.gameplay_menu_visible = True
                game.input_control = "main_menu"
                game.menu_main.main_menu_background.visible = False
                print "show main menu"
                self.last_pressed = False

    class PlayerFace(CreateSprite2):
        def __init__(self, name):
            super(Player.PlayerFace, self).__init__(name)
            self.description = "Next background"

        def do_action(self, game):
            pass



class PlayerCreationMenu():
    def __init__(self):
        self.visible = False
        self.input_control = False
        # DOWN BAR
        self.bar_down = (0, 600)
        # PORTRAIT POSITION
        self.portrait_position = (450, 100)

        self.player_portrait_position = (self.portrait_position[0]+100, self.portrait_position[1]+30)

        # Menu Background image

        self.background_image = load_sprite('player_creation_screen.png')

                # BUTTONS - player portrait

        # BUTTON NEXT FACE
        self.button_face_next = PlayerCreationMenu.ButtonPortraitFaceNext(
            'pc_right_arrow.png', (
                self.player_portrait_position[0]+105,
                self.player_portrait_position[1]+80))
        # BUTTON PREVIOUS FACE
        self.button_face_previous = PlayerCreationMenu.ButtonPortraitFacePrevious(
            'pc_left_arrow.png', (
                self.button_face_next.rect.x - 150,
                self.button_face_next.rect.y))
        # BUTTON NEXT BACKGROUND
        self.button_background_next = PlayerCreationMenu.ButtonPortraitBackgroundNext(
            'pc_right_arrow.png', (
                self.button_face_next.rect.x,
                self.button_face_next.rect.y+50))
        # BUTTON PREVIOUS BACKGROUND
        self.button_background_previous = PlayerCreationMenu.ButtonPortraitBackgroundPrevious(
            'pc_left_arrow.png', (
                self.button_face_previous.rect.x,
                self.button_background_next.rect.y))

                # BUTTONS - down bar

        # BUTTON FINISH
        self.button_finish = PlayerCreationMenu.ButtonFinish(
            'pc_button_finish.png',
            (self.bar_down[0]+900, self.bar_down[1]))

    def show_menu(self, screen, game):
        if game.player_creation_menu_visible is True:
            #MENU LOGIC
            sprite_group_background = pygame.sprite.Group(self.background_image)
            sprite_group_buttons = pygame.sprite.Group(
                self.button_face_next,
                self.button_face_previous,
                self.button_background_next,
                self.button_background_previous,
                self.button_finish
            )
            # INPUT
            for sprite in sprite_group_buttons:
                    sprite.get_state(game)
            # BUTTONS WORK if last pressed is true
            for button in sprite_group_buttons:
                button.do_action(game)
            #UPDATE
            sprite_group_background.update()
            sprite_group_buttons.update()

            #DISPLAY
            sprite_group_background.draw(screen)
            game.player.show_player_portrait(self.player_portrait_position, screen)
            sprite_group_buttons.draw(screen)

    # BUTTON CLASSES
        # DOWN BAR

    class ButtonFinish(CreateSprite2):
        def __init__(self, name,  position_tuple_x_y):
            super(PlayerCreationMenu.ButtonFinish, self).__init__(name, hover=True)
            self.description = "Next face"
            self.rect.x = position_tuple_x_y[0]
            self.rect.y = position_tuple_x_y[1]

        def do_action(self, game):
            if self.last_pressed is True:
                game.main_menu_visible = False
                game.player_creation_menu_visible = False
                game.gameplay_menu_visible = True
                game.input_control = "gameplay_menu"
                print "show game-play screen"
                self.last_pressed = False
        # PORTRAIT

    class ButtonPortraitFaceNext(CreateSprite2):
        def __init__(self, name,  position_tuple_x_y):
            super(PlayerCreationMenu.ButtonPortraitFaceNext, self).__init__(name, hover=True, pressed=True)
            self.description = "Next face"
            self.rect.x = position_tuple_x_y[0]
            self.rect.y = position_tuple_x_y[1]

        def do_action(self, game):
            if self.last_pressed is True:
                print "showing button !!!!"
                self.last_pressed = False

    class ButtonPortraitFacePrevious(CreateSprite2):
        def __init__(self, name,  position_tuple_x_y):
            super(PlayerCreationMenu.ButtonPortraitFacePrevious, self).__init__(name, hover=True, pressed=True)
            self.description = "Previous face"
            self.rect.x = position_tuple_x_y[0]
            self.rect.y = position_tuple_x_y[1]

        def do_action(self, game):
            pass

    class ButtonPortraitBackgroundNext(CreateSprite2):
        def __init__(self, name,  position_tuple_x_y):
            super(PlayerCreationMenu.ButtonPortraitBackgroundNext, self).__init__(name, hover=True, pressed=True)
            self.description = "Next background"
            self.rect.x = position_tuple_x_y[0]
            self.rect.y = position_tuple_x_y[1]

        def do_action(self, game):
            pass

    class ButtonPortraitBackgroundPrevious(CreateSprite2):
        def __init__(self, name,  position_tuple_x_y):
            super(PlayerCreationMenu.ButtonPortraitBackgroundPrevious, self).__init__(name, hover=True, pressed=True)
            self.description = "Previous background"
            self.rect.x = position_tuple_x_y[0]
            self.rect.y = position_tuple_x_y[1]

        def do_action(self, game):
            pass