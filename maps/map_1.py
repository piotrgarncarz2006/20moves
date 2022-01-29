# this file should be imported depending on current/selected map/level to file game.py

import pygame as pg
from settings import *
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


# every object on this map
world= [
        {'pos': {'x': 0, 'y': h- 50}, 'texture': textures['grass'], 'obj_class': 'grass'},
        {'pos': {'x': 0+ textures['grass'].get_width(), 'y': h- 50}, 'texture': textures['grass'], 'obj_class': 'grass'},
        {'pos': {'x': 0+ textures['grass'].get_width()* 2, 'y': h- 50}, 'texture': textures['grass'], 'obj_class': 'grass'},
        {'pos': {'x': 0+ textures['grass'].get_width()* 3, 'y': h- 50}, 'texture': textures['grass'], 'obj_class': 'grass'},
        {'pos': {'x': 0+ textures['grass'].get_width()* 4, 'y': h- 50}, 'texture': textures['grass'], 'obj_class': 'grass'},
        {'pos': {'x': 0+ textures['grass'].get_width()* 5, 'y': h- 50}, 'texture': textures['grass'], 'obj_class': 'grass'},
        {'pos': {'x': 0+ textures['grass'].get_width()* 6, 'y': h- 50}, 'texture': textures['grass'], 'obj_class': 'grass'},
        {'pos': {'x': 0+ textures['grass'].get_width()* 7, 'y': h- 50- 100}, 'texture': textures['grass'], 'obj_class': 'grass'},
        {'pos': {'x': 0+ textures['grass'].get_width()* 7, 'y': h- 50}, 'texture': textures['grass'], 'obj_class': 'grass'},

        {'pos': {'x': 0, 'y': h- 34- 64}, 'texture': textures['player_normal1'], 'obj_class': 'player'},
        ]
