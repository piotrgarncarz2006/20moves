#!/bin/python3
import pygame as pg
import os, sys
from math import *
#only for debuging remove in release
from pprint import pprint

def draw_bg(display, bg_col):
    display.fill(bg_col)

def render(display, world, bg_col, w, h, scale):
    draw_bg(display, bg_col)

    for el in world:
        display.blit(el['texture'], (el['pos']['x'], el['pos']['y']))

    pg.display.flip()

if __name__== '__main__':
    #TODO: import different maps with if statement
    from maps.map_1 import * #provides world, sources, bg, scale, textures

    pg.init()
    w, h= 1000, 500
    display= pg.display.set_mode((w, h))
    clock = pg.time.Clock()

    while True:
        clock.tick(60)
        for event in pg.event.get():
            if event.type== pg.QUIT: sys.exit()
        render(display, world, bg, w, h, scale)
