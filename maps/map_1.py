# this file should be imported depending on current/selected map/level to file game.py

import pygame as pg
import sys
import os
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
# adding the parent directory to 
# the sys.path.
sys.path.append(parent)
from settings.settings import *

# only for debuging remove in release
from pprint import pprint

# load one image with pygame.image.load and scales them using pg.transform.scale
def load_img(src, scale):
    img= pg.image.load(src) # load img from source to pygame obj type and save it in img variable
    return pg.transform.scale(img, (img.get_width()* scale, img.get_height()* scale)) # change img width and height

bg= (33, 38, 63) # bg of game window when using this map

# sources of images/textures
sources= {
        'grass': '/home/piotr/Programming/20moves/assets/img/grass.png',
        'key': '/home/piotr/Programming/20moves/assets/img/key.png',
        'player_normal1': '/home/piotr/Programming/20moves/assets/img/player_normal1.png',
        }

# loads images from sources
textures= {key: load_img(val, scale) for key, val in sources.items()}

hitbox_generation_rules= [
        {'obj_class': '*', 'change': {'y_top': 'y', 'y_bot': 'y+ height', 'x_left': 'x', 'x_right': 'x+ width'}},
        {'obj_class': 'grass', 'change': {'y_top': f'y+ {scale}* 4', 'y_bot': 'y+ height', 'x_left': 'x', 'x_right': 'x+ width'}},
        ]


# every object on this map
# 'colidable': 1 means true 0 means false -1 means false but generate hitbox
world= [
        {'pos': {'x': 0, 'y': h- 50}, 'texture': textures['grass'], 'colidable': 1, 'obj_class': 'grass'},
        {'pos': {'x': 1* textures['grass'].get_width(), 'y': h- 50}, 'texture': textures['grass'], 'colidable': 1, 'obj_class': 'grass'},
        {'pos': {'x': 2* textures['grass'].get_width(), 'y': h- 50}, 'texture': textures['grass'], 'colidable': 1, 'obj_class': 'grass'},
        {'pos': {'x': 3* textures['grass'].get_width(), 'y': h- 50}, 'texture': textures['grass'], 'colidable': 1, 'obj_class': 'grass'},
        {'pos': {'x': 4* textures['grass'].get_width(), 'y': h- 50}, 'texture': textures['grass'], 'colidable': 1, 'obj_class': 'grass'},
        {'pos': {'x': 5* textures['grass'].get_width(), 'y': h- 50}, 'texture': textures['grass'], 'colidable': 1, 'obj_class': 'grass'},
        {'pos': {'x': 6* textures['grass'].get_width(), 'y': h- 50}, 'texture': textures['grass'], 'colidable': 1, 'obj_class': 'grass'},
        {'pos': {'x': 7* textures['grass'].get_width(), 'y': h- 50- 100+ 50}, 'texture': textures['grass'], 'colidable': 1, 'obj_class': 'grass'},
        {'pos': {'x': 7* textures['grass'].get_width(), 'y': h- 50}, 'texture': textures['grass'], 'colidable': 1, 'obj_class': 'grass'},
        {'pos': {'x': 1* textures['grass'].get_width(), 'y': h- 50- 100+ 50}, 'texture': textures['grass'], 'colidable': 1, 'obj_class': 'grass'},

        {'pos': {'x': 180, 'y': h- 240}, 'texture': textures['grass'], 'colidable': 1, 'obj_class': 'grass'},
        {'pos': {'x': 180+ textures['grass'].get_width(), 'y': h- 240}, 'texture': textures['grass'], 'colidable': 1, 'obj_class': 'grass'},

        {'pos': {'x': 8* textures['grass'].get_width(), 'y': h- 50}, 'texture': textures['grass'], 'colidable': 1, 'obj_class': 'grass'},
        {'pos': {'x': 9* textures['grass'].get_width(), 'y': h- 50}, 'texture': textures['grass'], 'colidable': 1, 'obj_class': 'grass'},
        {'pos': {'x': 10* textures['grass'].get_width(), 'y': h- 50}, 'texture': textures['grass'], 'colidable': 1, 'obj_class': 'grass'},
        {'pos': {'x': 12* textures['grass'].get_width(), 'y': h- 50- 100}, 'texture': textures['grass'], 'colidable': 1, 'obj_class': 'grass'},
        {'pos': {'x': 13* textures['grass'].get_width(), 'y': h- 50- 100}, 'texture': textures['grass'], 'colidable': 1, 'obj_class': 'grass'},

        # player
        {'pos': {'x': 200, 'y': h- textures['player_normal1'].get_height()- textures['grass'].get_height()+ 1}, 'texture': textures['player_normal1'], 'colidable': 1, 'obj_class': 'player'},

        # key
        {'pos': {'x': 280, 'y': h- 80}, 'texture': textures['key'], 'colidable': -1, 'obj_class': 'key'},
        ]
