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
    from main import files_list
    #file_path = find(name)
    """
    fullname = os.path.join('data', name)
    """
    file_path = files_list.find_path(name)

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
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image2(name, True)

        self.true_position_x = self.rect.x
        self.true_position_y = self.rect.y


class Button(CreateSprite2):
    def __init__(self, name, hover=None, pressed=None):
        super(Button, self).__init__(name)
        self.visible = True
        # images
        self.image_no_hover = self.image
        self.image_hover = None
        self.image_pressed = None
        # button type
        self.type = 'normal'
        self.pressed = None
        # State in response to input
        self.last_pressed = False

        # check for hover and pressed images
        if hover is True:
            from main import files_list
            name_path = files_list.find_path(name)
            file_path, file_fullname = os.path.split(name_path)
            file_name, file_ending = os.path.splitext(file_fullname)
            self.image_hover = load_image2(file_name+"_hover"+file_ending)
        if pressed is True:
            from main import files_list
            name_path = files_list.find_path(name)
            file_path, file_fullname = os.path.split(name_path)
            file_name, file_ending = os.path.splitext(file_fullname)
            self.image_pressed = load_image2(file_name+"_pressed"+file_ending)

        if hover is True and pressed is True:
            self.type = 'hover,press'
        elif pressed is True and hover is not True:
            self.type = 'press'
        elif hover is True and pressed is not True:
            self.type = 'hover'

    def get_state(self, game):

        # LOCALS
        events = game.events
        mouse_hover = False
        mouse_button_down = False
        mouse_button_up = False
        #    is mouse over sprite ?
        if self.rect.collidepoint(game.mouse_position):
            mouse_hover = True
        else:
            mouse_hover = False

        #    is mouse button is down ?
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_button_down = True
            else:
                mouse_button_down = False
        #    is mouse button is up ?
        for event in game.key_mouse_event_list:
            if event == 'lmb_up':
                mouse_button_up = True
            else:
                mouse_button_up = False

        #    If mouse is on sprite and button is pressed up
        if mouse_button_up is True and mouse_hover is True:
            self.last_pressed = True
        else:
            self.last_pressed = False

        #######################################################

        # if there is pressed and hover image
        if self.type == 'hover,press':
            if self.rect.collidepoint(game.mouse_position):
                for event in game.key_mouse_event_list:
                    # pressed
                    if event == 'lmb_down':
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
        elif self.type == 'press':
            if self.rect.collidepoint(game.mouse_position):
                for event in events:
                    # pressed
                    if event == 'lmb_down':
                        self.image = self.image_pressed
                    # not pressed
                    else:
                        self.image = self.image_no_hover

        # if there is hover but there isn't pressed
        elif self.type == 'hover':
            if self.rect.collidepoint(game.mouse_position):
                self.image = self.image_hover
            else:
                if self.image != self.image_no_hover:
                    self.image = self.image_no_hover
