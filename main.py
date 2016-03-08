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

    def show_menu(self):
        if self.visible is True:
            main_menu_transparency = load_image('menu_transparency.png')
            main_menu_background = MainMenuBackground()
            middle_sprites = pygame.sprite.Group(main_menu_background)
            new_game_button = NewGameButton()
            top_sprites = pygame.sprite.Group(new_game_button)

            middle_sprites.update()
            top_sprites.update()

            screen.blit(main_menu_transparency[0], (0, 0))
            middle_sprites.draw(screen)
            top_sprites.draw(screen)
        else:
            pass


class MainMenuBackground(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('mainmenubackground.png')
        self.rect.x = 40
        self.rect.y = 40


class NewGameButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('newgame_normal.png')
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