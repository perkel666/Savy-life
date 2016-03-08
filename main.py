__author__ = 'Perkel'

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


class MainMenu():
    def __init__(self):
        self.visible = True
        self.position_x = 50
        self.position_y = 50

        self.continue_button = ContinueButton()
        self.newgame_button = NewGameButton()
        self.save_button = SaveButton()
        self.load_button = LoadButton()
        self.option_button = OptionsButton()
        self.quit_button = QuitButton()

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

            # 3. Creating Buttons sprite group from menu_options_active

            menu_buttons = pygame.sprite.Group()
            for button in menu_options_active:
                button.rect.y = (self.position_y - 50) + (75 * button.order)
                button.rect.x = self.position_x + 17
                menu_buttons.add(button)

            # UPDATE GRAPHIC
            main_menu_transparency = load_image('menu_transparency.png')
            main_menu_background = MainMenuBackground()
            middle_sprites = pygame.sprite.Group(main_menu_background)

            menu_buttons.update()
            middle_sprites.update()

            # DISPLAY
            screen.blit(main_menu_transparency[0], (0, 0))
            middle_sprites.draw(screen)
            menu_buttons.draw(screen)
        else:
            pass


class MainMenuBackground(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('mainmenubackground.png')
        self.rect.x = 40
        self.rect.y = 40


class ContinueButton(pygame.sprite.Sprite):
    def __init__(self):
        # TEMPLATE
        pygame.sprite.Sprite.__init__(self)
        # LOAD IMAGES AND SET RECTANGLE FOR SPRITE
        self.image, self.rect = load_image('continue_normal.png')
        self.image_hover, self.rect = load_image('continue_hover.png')
        self.imgae_no_hover = self.image
        # IS OPTION VISIBLE IN MENU
        self.visible = True
        # ORDER OF OPTION IN MENU
        self.order = 1
        # BUTTON POSITION ++++++ TO BE CHANGED
        self.rect.x = 65
        self.rect.y = 68

        # Functions that will do something
        # added some text


class NewGameButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('newgame_normal.png')
        self.image_hover, self.rect = load_image('newgame_hover.png')
        self.imgae_no_hover = self.image
        self.visible = True
        self.order = 2
        self.rect.x = 65
        self.rect.y = 68


class SaveButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('save_normal.png')
        self.image_hover, self.rect = load_image('save_hover.png')
        self.imgae_no_hover = self.image
        self.visible = True
        self.order = 3
        self.rect.x = 65
        self.rect.y = 68


class LoadButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('load_normal.png')
        self.image_hover, self.rect = load_image('load_hover.png')
        self.imgae_no_hover = self.image
        self.visible = True
        self.order = 4
        self.rect.x = 65
        self.rect.y = 68


class OptionsButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('options_normal.png')
        self.image_hover, self.rect = load_image('options_hover.png')
        self.imgae_no_hover = self.image
        self.visible = True
        self.order = 5
        self.rect.x = 65
        self.rect.y = 68


class QuitButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('quit_normal.png')
        self.image_hover, self.rect = load_image('quit_hover.png')
        self.imgae_no_hover = self.image
        self.visible = True
        self.order = 6
        self.rect.x = 65
        self.rect.y = 68


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


### MAIN GAME CLASS ########################################################
class Game(object):
    def main(self, screen_resolution):

        # GAME INITIALIZATION
        clock = pygame.time.Clock()
        main_menu = MainMenu()

        background_image = GameBackground()
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((200, 200, 200))
        while 1:

            clock.tick(50)

            # STATE OF THE GAME

            # GAME LOGIC

            # INPUT
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and pygame.K_ESCAPE:
                    return

            # DISPLAYING

            screen.blit(background, (0, 0))
            GameBackground.show_backgroud(background_image)
            MainMenu.show_menu(main_menu)

            pygame.display.flip()

            # SOUND AND MUSIC

##############################################################################

if __name__ == "__main__":
    pygame.init()
    screen_x = 1280
    screen_y = 720
    screen = pygame.display.set_mode((screen_x, screen_y))
    Game().main(screen)