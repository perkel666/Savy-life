__author__ = 'perkel666'

import pygame
import os


def load_image(name):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert_alpha()

    return image, image.get_rect()

# MAIN MENU
######################################################################
######################################################################
######################################################################


class MainMenu():
    def __init__(self):
        self.visible = True
        # MainMenu position
        self.position_x = 50
        self.position_y = 50
        # Buttons position relative to background position
        self.buttons_pos_x = 25
        self.buttons_pos_y = 40
        # Background image
        self.background = MainMenuBackground()
        self.background.rect.x = self.position_x
        self.background.rect.y = self.position_y
        # Background transparency
        self.transparency = MainMenuTransparency()
        # Buttons
        self.continue_button = ContinueButton()
        self.newgame_button = NewGameButton()
        self.save_button = SaveButton()
        self.load_button = LoadButton()
        self.option_button = OptionsButton()
        self.quit_button = QuitButton()
        # MainMenu background image layer
        self.mm_background = pygame.sprite.Group(self.background)
        # MainMenu transparency layer
        self.mm_transparency = pygame.sprite.Group(self.transparency)

    def show_menu(self):
        if self.visible is True:

            # MENU LOGIC
            # 1. Creating list of menu options

            menu_options = [
                self.continue_button,
                self.newgame_button,
                self.save_button,
                self.load_button,
                self.option_button,
                self.quit_button
            ]
            # 2. Creating list of visible menu options according to self.visible in button

            menu_options_active = []

            for menu_option in menu_options:
                if menu_option.visible is True:
                    menu_options_active.append(menu_option)

            # 3. Creating Buttons sprite group from menu_options_active and adding it to button layer

            mm_buttons = pygame.sprite.Group()
            for button in menu_options_active:
                # placement
                button.rect.y = (self.position_y - self.buttons_pos_y) + (75 * button.order)
                button.rect.x = self.position_x + self.buttons_pos_x
                # checks for mouse hove and if True then it changes
                # button image for _hover version
                if button.rect.collidepoint(pygame.mouse.get_pos()):
                    button.image = button.image_hover
                else:
                    if button.image != button.image_no_hover:
                        button.image = button.image_no_hover
                    else:
                        pass
                mm_buttons.add(button)

            # UPDATE MENU GRAPHIC

            self.mm_transparency.update()
            self.mm_background.update()
            mm_buttons.update()

            # DISPLAY
            self.mm_transparency.draw(screen)
            self.mm_background.draw(screen)
            mm_buttons.draw(screen)
        else:
            pass


class MainMenuTransparency(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('menu_transparency.png')


class MainMenuBackground(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('mainmenubackground.png')


class ContinueButton(pygame.sprite.Sprite):
    def __init__(self):
        # TEMPLATE
        pygame.sprite.Sprite.__init__(self)
        # LOAD IMAGES AND SET RECTANGLE FOR SPRITE
        self.image, self.rect = load_image('continue_normal.png')
        self.image_hover, self.rect = load_image('continue_hover.png')
        self.image_no_hover = self.image
        # IS OPTION VISIBLE IN MENU
        self.visible = True
        # ORDER OF OPTION IN MENU
        self.order = 1
        # METHODS


class NewGameButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('newgame_normal.png')
        self.image_hover, self.rect = load_image('newgame_hover.png')
        self.image_no_hover = self.image
        self.visible = True
        self.order = 2


class SaveButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('save_normal.png')
        self.image_hover, self.rect = load_image('save_hover.png')
        self.image_no_hover = self.image
        self.visible = True
        self.order = 3


class LoadButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('load_normal.png')
        self.image_hover, self.rect = load_image('load_hover.png')
        self.image_no_hover = self.image
        self.visible = True
        self.order = 4


class OptionsButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('options_normal.png')
        self.image_hover, self.rect = load_image('options_hover.png')
        self.image_no_hover = self.image
        self.visible = True
        self.order = 5


class QuitButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('quit_normal.png')
        self.image_hover, self.rect = load_image('quit_hover.png')
        self.image_no_hover = self.image
        self.visible = True
        self.order = 6

######################################################################
######################################################################
######################################################################


class GameBackground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('background.jpg')
        self.rect.x = 0
        self.rect.y = 0

    def show_backgroud(self):
        background = GameBackground()
        background_sprite = pygame.sprite.Group(background)
        background_sprite.update()
        background_sprite.draw(screen)


# MAIN GAME
######################################################################
######################################################################
######################################################################

class Game(object):
    def main(self, screen_resolution):

        # GAME INITIALIZATION
        running = True
        clock = pygame.time.Clock()
        main_menu = MainMenu()

        background_image = GameBackground()
        while running is True:

            clock.tick(50)

            # STATE OF THE GAME

            show_main_menu = True
            saves_present = True
            main_menu.visible = True

            # GAME LOGIC

            # INPUT
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and pygame.K_ESCAPE:
                    return
                if event.type == pygame.MOUSEBUTTONUP and \
                        event.button == 1 and \
                        main_menu.quit_button.rect.collidepoint(pygame.mouse.get_pos()):
                    main_menu.visible = False
                    running = False

            # DISPLAYING
            background_image.show_backgroud()
            main_menu.show_menu()

            pygame.display.flip()
            # SOUND AND MUSIC

##############################################################################

if __name__ == "__main__":
    pygame.init()
    screen_x = 1280
    screen_y = 720
    screen = pygame.display.set_mode((screen_x, screen_y))
    game = Game()
    game.main(screen)