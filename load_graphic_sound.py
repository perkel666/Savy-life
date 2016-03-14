__author__ = 'perkel666'

import os
import pygame


def find(name):
    for root, dirs, files in os.walk(os.curdir):
        if name in files:
            print os.path.join(root, name)
            return os.path.join(root, name)


def load_image(name):
    file_path = find(name)
    """
    fullname = os.path.join('data', name)
    """
    try:
        image = pygame.image.load(file_path)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert_alpha()

    return image, image.get_rect()


def load_sprite(name):
    class CreateSprite(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image, self.rect = load_image(name)
            self.visible = True

    sprite = CreateSprite()
    return sprite

## TESTING


def load_image2(name, rect=None):
    file_path = find(name)
    """
    fullname = os.path.join('data', name)
    """
    if rect is not None:
        try:
            image = pygame.image.load(file_path)
        except pygame.error, message:
            print 'Cannot load image:', name
            raise SystemExit, message
        image = image.convert_alpha()
        return image, image.get_rect()

    else:
        try:
            image = pygame.image.load(file_path)
        except pygame.error, message:
            print 'Cannot load image:', name
            raise SystemExit, message
        image = image.convert_alpha()
        return image


class CreateSprite2(pygame.sprite.Sprite):
    def __init__(self, name, hover=None, pressed=None):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image2(name, True)
        self.visible = True
        self.image_no_hover = self.image
        self.image_hover = None
        self.image_pressed = None
        # State in response to input
        self.last_pressed = False
        # State of buttons
        self.mouse_hover = False
        self.mouse_button_down = False
        self.mouse_button_up = False

        if hover is True:
            name_path = find(name)
            file_path, file_fullname = os.path.split(name_path)
            file_name, file_ending = os.path.splitext(file_fullname)
            self.image_hover = load_image2(file_name+"_hover"+file_ending)
        if pressed is True:
            name_path = find(name)
            file_path, file_fullname = os.path.split(name_path)
            file_name, file_ending = os.path.splitext(file_fullname)
            self.image_pressed = load_image2(file_name+"_pressed"+file_ending)

    def get_state2(self, game, events):

        mouse = pygame.mouse.get_pos()

                # STATE OF IMAGE INPUT

        if self.rect.collidepoint(mouse):
            self.mouse_hover = "Hover"
        else:
            self.mouse_hover = "No hover"

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.mouse_button_down = "MOUSE BUTTON DOWN"
            else:
                self.mouse_button_down = "MOUSE BUTTON NOT DOWN"
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.mouse_button_up = "MOUSE BUTTON UP"
            else:
                self.mouse_button_up = "MOUSE BUTTON NOT UP"
        print "=============="
        print self.mouse_hover
        print self.mouse_button_down
        print self.mouse_button_up



    def get_state(self, events):
        # CHANGES IMAGE BASED ON IF IMAGE HAS HOVER IMAGE
        # OR HOVER AND PRESSED IMAGE AND IF HAS NONE OF THOSE
        # THEN REGISTERS IF PLAYER HAS CLICKED ON IMAGE FOR USE LATER WITH METHOD
        # There is pressed and hover image

        """
        mouse_cursor = pygame.mouse.get_pos()
        if self.image_hover is not None and self.image_pressed is not None:
            if self.rect.collidepoint(mouse_cursor):
                for event in events:
                    # pressed
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        self.image = self.image_pressed
                        self.last_pressed = True
                    # not pressed
                    else:
                        self.image = self.image_hover
            else:
                if self.image != self.image_no_hover:
                    self.image = self.image_no_hover
                else:
                    pass
        # There is hover but there isn't pressed image
        elif self.image_hover is not None and self.image_pressed is None:
            if self.rect.collidepoint(mouse_cursor):
                self.image = self.image_hover
                for event in events:
                    # pressed
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        self.last_pressed = True
            else:
                if self.image != self.image_no_hover:
                    self.image = self.image_no_hover


            #if self.rect.collidepoint(pygame.mouse.get_pos()):
                #self.image = self.image_hover
            #else:
                #if self.image != self.image_no_hover:
                    #self.image = self.image_no_hover

        # There aren't any other images
        else:
            if self.rect.collidepoint(mouse_cursor):
                for event in events:
                    # pressed
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        self.last_pressed = True
        """