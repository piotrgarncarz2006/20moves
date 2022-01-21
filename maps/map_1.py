import pygame as pg
#only for debuging remove in release
from pprint import pprint

def load_img(src, scale):
    img= pg.image.load(src)
    return pg.transform.scale(img, (img.get_width()* scale, img.get_height()* scale))

scale= 4
bg= (67, 76, 94)

sources= {
        'grass': '/home/piotr/Py/20moves/assets/img/grass.png',
        }
textures= {key: load_img(val, scale) for key, val in sources.items()}

world= [
        {'pos': {'x': 0, 'y': 0}, 'texture': textures['grass']},
        {'pos': {'x': 0+ textures['grass'].get_width(), 'y': 0}, 'texture': textures['grass']},
        ]
