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

    def get_state(self):

        # if there is pressed and hover image
        if self.image_hover is not None and \
                self.image_pressed is not None:

            if self.rect.collidepoint(pygame.mouse.get_pos()):
                for event in pygame.event.get():
                    # pressed
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        self.image = self.image_pressed
                    # not pressed
                    else:
                        self.image = self.image_hover
            else:
                if self.image != self.image_no_hover:
                    self.image = self.image_no_hover
                else:
                    pass
        # if there is hover but there isn't pressed
        elif self.image_hover is not None and self.image_pressed is None:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.image = self.image_hover
            else:
                if self.image != self.image_no_hover:
                    self.image = self.image_no_hover
        else:
            pass