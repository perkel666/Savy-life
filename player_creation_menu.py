__author__ = 'perkel666'
import pygame


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
        self.player_portrait = None
        self.player_background = None
        # health and stamina
        self.health = 0
        self.stamina = 0
        # Base statistics
        self.strenght = 5
        self.endurance = 5
        self.agility = 5
        self.percepcion = 5
        self.inteligence = 5
        self.agility = 5
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
    def __init__(self):
        self.visible = False
        # Create player
        #Background image
        self.background_image = ""


    def show_menu(self, game, screen):
