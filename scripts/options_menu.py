__author__ = 'Perkel'


from scripts.load_graphic_sound import *


class OptionsMenu():
    def __init__(self):
        self.visible = False
        self.input_control = False

        # UI POSITIONING
        self.position_options_menu = (50, 50)
        self.position_main_buttons = (self.position_options_menu[0]+30, self.position_options_menu[1]+40)
        self.position_main_buttons_difference_y = 75
        self.position_submenu = (self.position_options_menu[0]+275, self.position_options_menu[1]+40)
        self.position_submenu_button_display_mode = (self.position_submenu[0]+400, self.position_submenu[1]+30)

        # UI INITIALIZATION
                    # main options menu
        self.ui_transparency = OptionsMenu.UITransparency('menu_transparency.png')
        self.ui_background = OptionsMenu.UIBackground('options_menu_background.png')
                    # buttons main
        self.ui_button_game = OptionsMenu.UIButtonGame('button_game.png')
        self.ui_button_display = OptionsMenu.UIButtonDisplay('button_display.png')
        self.ui_button_sound = OptionsMenu.UIButtonSound('button_sound.png')
        self.ui_button_back = OptionsMenu.UIButtonBack('button_back.png')
                    # buttons display
        self.ui_button_display_set_mode = OptionsMenu.UIButtonDisplaySetMode('button_state_off.png')
                    # background submenus
        self.ui_submenu_game = OptionsMenu.UIGameBackground('body_game.png')
        self.ui_submenu_display = OptionsMenu.UIDisplayBackground('body_display.png')
        self.ui_submenu_sound = OptionsMenu.UISoundBackground('body_sound.png')
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
            layer_submenu_buttons = pygame.sprite.Group()
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
                        # buttons main
            difference = 0
            for button in self.ui_buttons_list:
                button.rect.x = position_main_buttons[0]
                button.rect.y = position_main_buttons[1] + difference
                difference += position_main_buttons_difference_y
                        # buttons submenu                                 ################### WORK
            self.ui_button_display_set_mode.rect.x = self.position_submenu_button_display_mode[0]
            self.ui_button_display_set_mode.rect.y = self.position_submenu_button_display_mode[1]

            # CHANGE STATE AND INPUT
                        # buttons
            if game.input_control is "options_menu":
                for button in self.ui_buttons_list:
                    button.get_state(game)

            if game.input_control is "options_menu":
                if self.ui_button_display_set_mode.visible is True:
                    self.ui_button_display_set_mode.get_state(game)

            # OUTPUT
            if game.input_control is "options_menu":
                for button in self.ui_buttons_list:
                    button.do_action(game)

            if self.ui_submenu_display.visible is True:
                self.ui_button_display_set_mode.visible = True

            if game.input_control is "options_menu":
                if self.ui_button_display_set_mode.visible is True:
                    self.ui_button_display_set_mode.do_action(game)

            # ADD SPRITES TO LAYERS

            for submenu in self.ui_submenus_list:
                if submenu.visible is True:
                    layer_submenus.add(submenu)

            if self.ui_button_display_set_mode.visible is True:
                layer_submenu_buttons.add(self.ui_button_display_set_mode)

            for button in self.ui_buttons_list:
                if button.visible is True:
                    layer_buttons_top.add(button)

            # UPDATE

            layer_transparency.update()
            layer_background.update()
            layer_submenus.update()
            layer_buttons_down.update()
            layer_buttons_top.update()
            layer_submenu_buttons.update()

            # DISPLAY

            layer_transparency.draw(screen)
            layer_background.draw(screen)
            layer_submenus.draw(screen)
            layer_buttons_down.draw(screen)
            layer_buttons_top.draw(screen)
            layer_submenu_buttons.draw(screen)

    ##################################
    # CLASSES used in OptionsMenu() #
    ##################################

        # first screen
    class UITransparency(Button):
        def __init__(self, name):
            super(OptionsMenu.UITransparency, self).__init__(name)

    class UIBackground(Button):
        def __init__(self, name):
            super(OptionsMenu.UIBackground, self).__init__(name)

        # buttons main
    class UIButtonGame(Button):
        def __init__(self, name):
            super(OptionsMenu.UIButtonGame, self).__init__(name, hover=True)
            self.visible = True

        def do_action(self, game):
            if self.last_pressed is True:
                self.last_pressed = False
                game.menu_options.ui_submenu_game.visible = True
                game.menu_options.ui_submenu_display.visible = False
                game.menu_options.ui_submenu_sound.visible = False
                print "button_game"

    class UIButtonDisplay(Button):
        def __init__(self, name):
            super(OptionsMenu.UIButtonDisplay, self).__init__(name, hover=True)
            self.visible = True

        def do_action(self, game):
            if self.last_pressed is True:
                self.last_pressed = False
                game.menu_options.ui_submenu_game.visible = False
                game.menu_options.ui_submenu_display.visible = True
                game.menu_options.ui_submenu_sound.visible = False
                print "button_display"

    class UIButtonSound(Button):
        def __init__(self, name):
            super(OptionsMenu.UIButtonSound, self).__init__(name, hover=True)
            self.visible = True

        def do_action(self, game):
            if self.last_pressed is True:
                self.last_pressed = False
                game.menu_options.ui_submenu_game.visible = False
                game.menu_options.ui_submenu_display.visible = False
                game.menu_options.ui_submenu_sound.visible = True
                print "button_sound"

    class UIButtonBack(Button):
        def __init__(self, name):
            super(OptionsMenu.UIButtonBack, self).__init__(name, hover=True)
            self.visible = True

        def do_action(self, game):
            if self.last_pressed is True:
                self.last_pressed = False
                game.main_menu_visible = True
                game.options_menu_visible = False
                game.update_input_control = "main_menu"
                print "button_back"

                # buttons display
    class UIButtonDisplaySetMode(Button):
        def __init__(self, name):
            super(OptionsMenu.UIButtonDisplaySetMode, self).__init__(name, hover=True)
            self.visible = False
            self.image_on = Button('button_state_on.png', hover=True)
            self.image_off = Button('button_state_off.png', hover=True)
            self.on = False

        def do_action(self, game):
            if self.last_pressed is True:
                self.last_pressed = False
                if self.on is False:
                    self.on = True
                    game.fullscreen = True
                    self.image = self.image_on.image
                    self.image_hover = self.image_on.image_hover
                    print "fullscreen ON"

                elif self.on is True:
                    self.on = False
                    game.fullscreen = False
                    self.image = self.image_off.image
                    self.image_hover = self.image_off.image_hover
                    print "fullscreen OFF"


        # background to option right screens
    class UIGameBackground(Button):
        def __init__(self, name):
            super(OptionsMenu.UIGameBackground, self).__init__(name)
            self.visible = True

    class UIDisplayBackground(Button):
        def __init__(self, name):
            super(OptionsMenu.UIDisplayBackground, self).__init__(name)
            self.visible = False

    class UISoundBackground(Button):
        def __init__(self, name):
            super(OptionsMenu.UISoundBackground, self).__init__(name)
            self.visible = False