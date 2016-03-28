__author__ = 'perkel666'

from scripts.load_graphic_sound import *
from scripts.sprite_effects import *


class Player():
    def __init__(self):
        # Basic info
        self.name = "Enter Name"
        self.sex = "male"
        self.money = 0
        # Portrait
        self.path_faces = "data/art/player/head"
        self.path_backgrounds = "data/art/player/backgrounds"

        self.list_faces = os.listdir(self.path_faces)
        self.list_background = os.listdir(self.path_backgrounds)
        self.current_face = 0
        self.current_background = 0

        self.player_portrait = Player.PlayerFace(self.list_faces[self.current_face])
        self.player_background = Player.PlayerBackground(self.list_background[self.current_background])

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
        # Back-story

    # CHANGING FACE AND BACKGROUND
    def change_face_next(self, game):
        self.current_face += 1
        if self.current_face > len(self.list_faces)-1:
            self.current_face = 0
        print "current face ", self.current_face
        portrait = game.player.PlayerFace(self.list_faces[self.current_face])
        self.player_portrait = portrait

    def change_face_previous(self, game):
        self.current_face -= 1
        if self.current_face < 0:
            self.current_face = len(self.list_faces)-1
        print "current face ", self.current_face
        portrait = game.player.PlayerFace(self.list_faces[self.current_face])
        self.player_portrait = portrait

    def change_background_next(self, game):
        self.current_background += 1
        if self.current_background > len(self.list_background)-1:
            self.current_background = 0
        print "current background ", self.current_background
        background = game.player.PlayerBackground(self.list_background[self.current_background])
        self.player_background = background

    def change_background_previous(self, game):
        self.current_background -= 1
        if self.current_background < 0:
            self.current_background = len(self.list_background)-1
        print "current background ", self.current_background
        background = game.player.PlayerBackground(self.list_background[self.current_background])
        self.player_background = background

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
        #DISPLAY
        layer_background.draw(screen)
        layer_face.draw(screen)

    class PlayerBackground(Button):
        def __init__(self, name):
            super(Player.PlayerBackground, self).__init__(name)
            self.description = "Next background"

        def do_action(self, game):
            if self.last_pressed is True:
                self.last_pressed = False
                game.menu_main.visible = True
                game.menu_gameplay.visible = True

                game.update_input_control = "main_menu"
                game.menu_main.panorama.visible = False
                game.menu_main.main_menu_transparency.visible = True
                print "show main menu"

    class PlayerFace(Button):
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

        # BUTTONS LIST:
        self.buttons_list = [
            self.button_face_next,
            self.button_face_previous,
            self.button_background_next,
            self.button_background_previous,
            self.button_finish
        ]

    def show_menu(self, screen, game):
        if game.menu_player_creation.visible is True:
            #MENU LOGIC

            # INPUT
            for button in self.buttons_list:
                    button.get_state(game)

            sprite_group_background = pygame.sprite.Group(self.background_image)
            sprite_group_buttons = pygame.sprite.Group()

            for button in self.buttons_list:
                sprite_group_buttons.add(button)

            # DISPLAY
            sprite_group_background.draw(screen)
            game.player.show_player_portrait(self.player_portrait_position, screen)
            sprite_group_buttons.draw(screen)

            # ACTION

            # BUTTONS WORK if last pressed is true
            for button in sprite_group_buttons:
                button.do_action(game)




    # BUTTON CLASSES
        # DOWN BAR

    class ButtonFinish(Button):
        def __init__(self, name,  position_tuple_x_y):
            super(PlayerCreationMenu.ButtonFinish, self).__init__(name, hover=True)
            self.description = "Next face"
            self.rect.x = position_tuple_x_y[0]
            self.rect.y = position_tuple_x_y[1]

        def do_action(self, game):
            if self.last_pressed is True:
                self.last_pressed = False

                game.menu_main.visible = False
                game.menu_gameplay.visible = True
                game.menu_player_creation.visible = False

                game.update_input_control = "gameplay_menu"

        # PORTRAIT

    class ButtonPortraitFaceNext(Button):
        def __init__(self, name,  position_tuple_x_y):
            super(PlayerCreationMenu.ButtonPortraitFaceNext, self).__init__(name, hover=True, pressed=True)
            self.description = "Next face"
            self.rect.x = position_tuple_x_y[0]
            self.rect.y = position_tuple_x_y[1]

        def do_action(self, game):
            if self.last_pressed is True:
                game.player.change_face_next(game)
                print self.description
                self.last_pressed = False


    class ButtonPortraitFacePrevious(Button):
        def __init__(self, name,  position_tuple_x_y):
            super(PlayerCreationMenu.ButtonPortraitFacePrevious, self).__init__(name, hover=True, pressed=True)
            self.description = "Previous face"
            self.rect.x = position_tuple_x_y[0]
            self.rect.y = position_tuple_x_y[1]

        def do_action(self, game):
            if self.last_pressed is True:
                game.player.change_face_previous(game)
                print self.description
                self.last_pressed = False

    class ButtonPortraitBackgroundNext(Button):
        def __init__(self, name,  position_tuple_x_y):
            super(PlayerCreationMenu.ButtonPortraitBackgroundNext, self).__init__(name, pressed=True)
            self.description = "Next background"
            self.rect.x = position_tuple_x_y[0]
            self.rect.y = position_tuple_x_y[1]

        def do_action(self, game):
            if self.last_pressed is True:
                game.player.change_background_next(game)
                print self.description
                self.last_pressed = False

    class ButtonPortraitBackgroundPrevious(Button):
        def __init__(self, name,  position_tuple_x_y):
            super(PlayerCreationMenu.ButtonPortraitBackgroundPrevious, self).__init__(name, hover=True, pressed=True)
            self.description = "Previous background"
            self.rect.x = position_tuple_x_y[0]
            self.rect.y = position_tuple_x_y[1]

        def do_action(self, game):
            if self.last_pressed is True:
                game.player.change_background_previous(game)
                print self.description
                self.last_pressed = False