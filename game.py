#!/bin/python3

# this file should be executed from game launcher with proper arguments shuch as window width and height, current map, fps limit, current character, etc.

import pygame as pg
import os, sys
from math import *
# only for debuging remove in release
from pprint import pprint

# TODO: import different maps with if statement
from maps.map_1 import * # provides world, sources, bg, scale, textures

pg.init()
w, h= 1000, 500 # size of window
display= pg.display.set_mode((w, h)) # creates window
clock = pg.time.Clock() # clock to limit fps
fps= 60 # fps limit

# every event that changes something on game map located in world list. Format of event_queue: [ { (text) 'action', (text) 'target', (int) 'frames', additional arguments } ] where frames is on how many frames event will execute this values is decremented every frame by event_handler()
event_queue= []

# fills background to solid color
def draw_bg():
    display.fill(bg) # change bg color of window saved in display variable

# draws every object from world list
def draw_world():
    # world[] contains every object located on current level/map
    for el in world:
        display.blit(el['texture'], (el['pos']['x'], el['pos']['y']))

# renders background and objects from world list
def render():
    draw_bg()
    draw_world()

    pg.display.flip() # shows newly rendered elements

# move object from world list
def move(obj_class, speed_x, speed_y):
    for e in world:
        if e['obj_class']== obj_class:
            e['pos']['x']+= speed_x
            e['pos']['y']+= speed_y

# executes single event from event_queue
def exec_event(ev):
    if ev['action']== 'mv':
        move(ev['target'], ev['x'], ev['y'])

# handles/executes events from event_queue
def event_handler():
    delete_marks= []
    for ev in event_queue:
        ev['frames']-= 1
        exec_event(ev)
        if ev['frames']<= 0:
            delete_marks.append(ev)
    for ev in delete_marks:
        event_queue.remove(ev)

# check if key has been pressed and exec its action
def check_keys():
    # loop through pygame events such as keyboard events
    # put key shortcuts in this loop
    for event in pg.event.get():
        if event.type== pg.QUIT: sys.exit()
        if event.type== pg.KEYDOWN:
            if event.key== pg.K_d:
                event_queue.append({'action': 'mv', 'target': 'player', 'frames': 20, 'x': 12.4, 'y': 0})
            if event.key== pg.K_a:
                event_queue.append({'action': 'mv', 'target': 'player', 'frames': 20, 'x': -12.4, 'y': 0})

# executes before render function
def prerender():
    check_keys()
    event_handler() # executes events from event_queue

# game loop
while True:
    clock.tick(fps) # limits fps to value of fps variable
    prerender() # handling hotkeys, event_queue, etc.
    render() # draws objects and background
