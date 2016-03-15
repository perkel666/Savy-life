__author__ = 'Perkel'


from load_graphic_sound import *


class OptionsMenu():
    def __init__(self):
        self.visible = False
        self.input_control = False

        # UI POSITIONING
        self.position_options_menu = (50, 50)
        self.position_main_buttons = (self.position_options_menu[0]+30, self.position_options_menu[1]+40)
        self.position_main_buttons_difference_y = 75
        self.position_submenu = (self.position_options_menu[0]+275, self.position_options_menu[1]+40)

        # UI INITIALIZATION
                    # main options menu
        self.ui_transparency = OptionsMenu.UITransparency('menu_transparency.png')
        self.ui_background = OptionsMenu.UIBackground('options_menu_background.png')
                    # buttons
        self.ui_button_game = OptionsMenu.UIButtonGame('button_game.png')
        self.ui_button_display = OptionsMenu.UIButtonDisplay('button_display.png')
        self.ui_button_sound = OptionsMenu.UIButtonSound('button_sound.png')
        self.ui_button_back = OptionsMenu.UIButtonBack('button_back.png')
                    # buttons submenus
        self.ui_submenu_game = OptionsMenu.UIGameBackground('options_menu_body.png')
        self.ui_submenu_display = OptionsMenu.UIDisplayBackground('options_menu_body.png')
        self.ui_submenu_sound = OptionsMenu.UISoundBackground('options_menu_body.png')
                    # lists
        self.ui_buttons_list = [
            self.ui_button_game,
            self.ui_button_display,
            self.ui_button_sound,
            self.ui_button_back]

        self.ui_submenus_list = [
            self.ui_submenu_game,
            self.ui_submenu_display,
            self.ui_submenu_sound]

    def show_menu(self, screen, game):
        if game.options_menu_visible is True:

            # LOCALS
                    # position
            position_transparency = (0, 0)
            position_options_menu = self.position_options_menu
            position_main_buttons = self.position_main_buttons
            position_main_buttons_difference_y = self.position_main_buttons_difference_y
            position_submenu = self.position_submenu

                    # sprite layers
            layer_transparency = pygame.sprite.Group()
            layer_background = pygame.sprite.Group()
            layer_submenus = pygame.sprite.Group()
            layer_buttons_down = pygame.sprite.Group()
            layer_buttons_top = pygame.sprite.Group()
            #layer_
            #layer_

            # UI POSITIONING
                        # transparency
            self.ui_transparency.rect.x = position_transparency[0]
            self.ui_transparency.rect.y = position_transparency[1]
            layer_transparency.add(self.ui_transparency)
                        # background
            self.ui_background.rect.x = position_options_menu[0]
            self.ui_background.rect.y = position_options_menu[1]
            layer_background.add(self.ui_background)
                        # submenus
            for submenu in self.ui_submenus_list:
                submenu.rect.x = position_submenu[0]
                submenu.rect.y = position_submenu[1]
                        # buttons
            difference = 0
            for button in self.ui_buttons_list:
                button.rect.x = position_main_buttons[0]
                button.rect.y = position_main_buttons[1] + difference
                difference += position_main_buttons_difference_y

            # CHANGE STATE AND INPUT
                        # buttons
            if game.input_control is "options_menu":
                for button in self.ui_buttons_list:
                    button.get_state(game)

            # OUTPUT
            if game.input_control is "options_menu":
                for button in self.ui_buttons_list:
                    button.do_action(game)

            # ADD SPRITES TO LAYERS

            for submenu in self.ui_submenus_list:
                if submenu.visible is True:
                    layer_submenus.add(submenu)

            for button in self.ui_buttons_list:
                if button.visible is True:
                    layer_buttons_top.add(button)

            # UPDATE

            layer_transparency.update()
            layer_background.update()
            layer_submenus.update()
            layer_buttons_down.update()
            layer_buttons_top.update()

            # DISPLAY

            layer_transparency.draw(screen)
            layer_background.draw(screen)
            layer_submenus.draw(screen)
            layer_buttons_down.draw(screen)
            layer_buttons_top.draw(screen)

    ##################################
    # CLASSES used in OptionsMenu() #
    ##################################

        # first screen
    class UITransparency(CreateSprite2):
        def __init__(self, name):
            super(OptionsMenu.UITransparency, self).__init__(name)

    class UIBackground(CreateSprite2):
        def __init__(self, name):
            super(OptionsMenu.UIBackground, self).__init__(name)

        # buttons
    class UIButtonGame(CreateSprite2):
        def __init__(self, name):
            super(OptionsMenu.UIButtonGame, self).__init__(name, hover=True)
            self.visible = True

        def do_action(self, game):
            if self.last_pressed is True:
                print "button_game"
                self.last_pressed = False

    class UIButtonDisplay(CreateSprite2):
        def __init__(self, name):
            super(OptionsMenu.UIButtonDisplay, self).__init__(name, hover=True)
            self.visible = True

        def do_action(self, game):
            if self.last_pressed is True:
                print "button_display"
                self.last_pressed = False

    class UIButtonSound(CreateSprite2):
        def __init__(self, name):
            super(OptionsMenu.UIButtonSound, self).__init__(name, hover=True)
            self.visible = True

        def do_action(self, game):
            if self.last_pressed is True:
                print "button_sound"
                self.last_pressed = False

    class UIButtonBack(CreateSprite2):
        def __init__(self, name):
            super(OptionsMenu.UIButtonBack, self).__init__(name, hover=True)
            self.visible = True

        def do_action(self, game):
            if self.last_pressed is True:
                self.last_pressed = False
                game.main_menu_visible = True
                game.options_menu_visible = False
                game.input_control = "main_menu"
                print "button_back"


        # background to option right screens
    class UIGameBackground(CreateSprite2):
        def __init__(self, name):
            super(OptionsMenu.UIGameBackground, self).__init__(name)
            self.visible = True

    class UIDisplayBackground(CreateSprite2):
        def __init__(self, name):
            super(OptionsMenu.UIDisplayBackground, self).__init__(name)
            self.visible = False

    class UISoundBackground(CreateSprite2):
        def __init__(self, name):
            super(OptionsMenu.UISoundBackground, self).__init__(name)
            self.visible = False