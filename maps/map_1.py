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
    img= pg.image.load(src)
    return pg.transform.scale(img, (img.get_width()* scale, img.get_height()* scale))

scale= 4 # scale in which draw_world() will draw objects from world list
bg= (33, 38, 63) # bg of game window when using this map

# sources of images/textures
sources= {
        'grass': '/home/piotr/Py/20moves/assets/img/grass.png',
        'player_normal1': '/home/piotr/Py/20moves/assets/img/player_normal1.png',
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
        {'pos': {'x': 0+ textures['grass'].get_width(), 'y': h- 50}, 'texture': textures['grass'], 'colidable': 1, 'obj_class': 'grass'},
        {'pos': {'x': 0+ textures['grass'].get_width()* 2, 'y': h- 50}, 'texture': textures['grass'], 'colidable': 1, 'obj_class': 'grass'},
        {'pos': {'x': 0+ textures['grass'].get_width()* 3, 'y': h- 50}, 'texture': textures['grass'], 'colidable': 1, 'obj_class': 'grass'},
        {'pos': {'x': 0+ textures['grass'].get_width()* 4, 'y': h- 50}, 'texture': textures['grass'], 'colidable': 1, 'obj_class': 'grass'},
        {'pos': {'x': 0+ textures['grass'].get_width()* 5, 'y': h- 50}, 'texture': textures['grass'], 'colidable': 1, 'obj_class': 'grass'},
        {'pos': {'x': 0+ textures['grass'].get_width()* 6, 'y': h- 50}, 'texture': textures['grass'], 'colidable': 1, 'obj_class': 'grass'},
        {'pos': {'x': 0+ textures['grass'].get_width()* 7, 'y': h- 50- 100}, 'texture': textures['grass'], 'colidable': 1, 'obj_class': 'grass'},
        {'pos': {'x': 0+ textures['grass'].get_width()* 7, 'y': h- 50}, 'texture': textures['grass'], 'colidable': 1, 'obj_class': 'grass'},

        {'pos': {'x': 0, 'y': h- 34- 64}, 'texture': textures['player_normal1'], 'colidable': 1, 'obj_class': 'player'},
        ]
