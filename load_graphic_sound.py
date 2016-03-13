__author__ = 'perkel666'

import os
import pygame


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


def find(name):
    for root, dirs, files in os.walk(os.curdir):
        if name in files:
            print os.path.join(root, name)
            return os.path.join(root, name)


def load_image_2(name, rect=None):
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


def load_spriter(name, hover=None, pressed=None):
    class CreateSprite(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image, self.rect = load_image(name)
            self.visible = True

            # PRESSED AND HOVER NEEDS TO BE SAME SIZE
            # TO WORK PROPERLY IN GAME
            if hover is not None and hover is True:
                self.image_no_hover = self.image
                path, ext = os.path.splitext(name)
                self.image_hover = load_image_2(find(path+'_hover.png'))
            elif hover is not None and hover is not True:
                print "hover shound be True got something else instead for ", name
            if pressed is not None and pressed is True:
                path, ext = os.path.splitext(name)
                self.image_pressed = load_image_2(find(path+'_pressed.png'))
            elif pressed is not None and pressed is not True:
                print "pressed shoud be True got something else instead for ", name

        def get_state(self):

            # if there is pressed and hover image
            if self.image_hover is not None and \
                    self.image_pressed is not None:

                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    for event in pygame.event.get():
                        # pressed
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            sprite.image = sprite.image_pressed
                        # not pressed
                        else:
                            sprite.image = sprite.image_hover
                else:
                    if sprite.image != sprite.image_no_hover:
                        sprite.image = sprite.image_no_hover
                    else:
                        pass
            # if there is hover but there isn't pressed
            elif self.image_hover is not None and self.image_pressed is None:
                if sprite.rect.collidepoint(pygame.mouse.get_pos()):
                    sprite.image = sprite.image_hover
                else:
                    if sprite.image != sprite.image_no_hover:
                        sprite.image = sprite.image_no_hover
            else:
                pass



    sprite = CreateSprite()
    return sprite