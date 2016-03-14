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


class PlayerCreationMenu():
    def __init__(self, game):
        self.visible = False
        # DOWN BAR
        self.bar_down = (0, 600)
        # PORTRAIT POSITION
        self.portrait_position = (450, 100)
        # MAIN STATS POSITION
        # SKILLS POSITION
        # HEALTH STAMINA POSITION
        # choose player head
        self.player_portrait_position = (self.portrait_position[0]+100, self.portrait_position[1]+30)
        player_portrait_list = os.listdir('data/art/player/head')
        player_background_list = os.listdir('data/art/player/backgrounds')
        game.player.player_portrait = load_sprite(player_portrait_list[1])
        game.player.player_background = load_sprite(player_background_list[2])

        # Menu Background image

        self.background_image = load_sprite('player_creation_screen.png')
        self.background_image.rect.x = 0
        self.background_image.rect.y = 0

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
            sprite_group_buttons2 = pygame.sprite.Group(
                self.button_face_next,
                self.button_face_previous,
                self.button_background_next,
                self.button_background_previous,
                self.button_finish
            )

            for sprite in sprite_group_buttons2:
                    sprite.get_state()

            if game.input_control is "player_creation_menu":
                for sprite in sprite_group_buttons2:
                    sprite.do_action(game)
            """
            #INPUT
            if game.input_control is "player_creation_menu":
                for event in pygame.event.get():
                    # BACKGROUND CLICK === > MAIN MENU
                    if event.type == pygame.MOUSEBUTTONUP and \
                            event.button == 1 and \
                            self.button_finish.rect.collidepoint(pygame.mouse.get_pos()):
                        game.main_menu_visible = False
                        game.player_creation_menu_visible = False
                        game.gameplay_menu_visible = True
                        game.input_control = "gameplay_menu"
                        print "show game-play screen"
                    elif event.type == pygame.MOUSEBUTTONUP and \
                            event.button == 1 and \
                            self.button_face_next.rect.collidepoint(pygame.mouse.get_pos()):
                        print "showing button !!!!"
            """
            #UPDATE
            sprite_group_background.update()
            sprite_group_buttons2.update()

            #DISPLAY
            sprite_group_background.draw(screen)
            game.player.show_player_portrait(self.player_portrait_position, screen)
            sprite_group_buttons2.draw(screen)

    # BUTTON CLASSES
        # DOWN BAR
    class ButtonFinish(CreateSprite2):
        def __init__(self, name,  position_tuple_x_y):
            super(PlayerCreationMenu.ButtonFinish, self).__init__(name, hover=True,)
            self.description = "Next face"
            self.rect.x = position_tuple_x_y[0]
            self.rect.y = position_tuple_x_y[1]

        def show_description(self):
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                return self.description

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

        def show_description(self):
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                return self.description

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

        def show_description(self):
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                return self.description

        def do_action(self, game):
            pass

    class ButtonPortraitBackgroundNext(CreateSprite2):
        def __init__(self, name,  position_tuple_x_y):
            super(PlayerCreationMenu.ButtonPortraitBackgroundNext, self).__init__(name, hover=True, pressed=True)
            self.description = "Next background"
            self.rect.x = position_tuple_x_y[0]
            self.rect.y = position_tuple_x_y[1]

        def show_description(self):
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                return self.description

        def do_action(self, game):
            pass

    class ButtonPortraitBackgroundPrevious(CreateSprite2):
        def __init__(self, name,  position_tuple_x_y):
            super(PlayerCreationMenu.ButtonPortraitBackgroundPrevious, self).__init__(name, hover=True, pressed=True)
            self.description = "Previous background"
            self.rect.x = position_tuple_x_y[0]
            self.rect.y = position_tuple_x_y[1]

        def show_description(self):
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                return self.description

        def do_action(self, game):
            pass