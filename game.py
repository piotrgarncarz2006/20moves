#!/bin/python3

# this file should be executed from game launcher with proper arguments shuch as window width and height, current map, fps limit, current character, etc.

import pygame as pg
import os, sys
from math import *
from settings import *
# only for debuging remove in release
from pprint import pprint

# TODO: import different maps with if statement
from maps.map_1 import * # provides world, sources, bg, scale, textures

pg.init() # allows to use pygame methods
font= pg.font.SysFont('monospace', 24)
display= pg.display.set_mode((w, h)) # creates window
clock = pg.time.Clock() # clock to limit fps
fps= 60 # fps limit
moves_left= 20 # how many moves can you make
minimum_distance_from_border= 100 # minimum distance of player to screen border before viewport moves
viewport_movement_value= 400 # value by which viewport moves when distance from screen border is lesser than minimum_distance_from_border. This value can be negative or positive depending on from which border distance is lesser than minimum_distance_from_border

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

def show_move_counter():
    counter= font.render(f'Moves: {moves_left}', 1, (49, 228, 201))
    display.blit(counter, (850, 20))

# renders background and objects from world list and displays text
def render():
    draw_bg()
    draw_world()
    show_move_counter()

    pg.display.flip() # shows newly rendered elements

# move object from world list
def move(obj_class, speed_x, speed_y):
    for e in world:
        if e['obj_class']== obj_class:
            e['pos']['x']+= speed_x
            e['pos']['y']+= speed_y

def get_player_width():
    for e in world:
        if e['obj_class']== 'player':
            return e['texture'].get_width()

def get_player_height():
    for e in world:
        if e['obj_class']== 'player':
            return e['texture'].get_height()

def get_player_x():
    for e in world:
        if e['obj_class']== 'player':
            return e['pos']['x']

def get_player_y():
    for e in world:
        if e['obj_class']== 'player':
            return e['pos']['y']

def get_player_x_and_y():
    for e in world:
        if e['obj_class']== 'player':
            return [e['pos']['x'], e['pos']['y']]

# moves viewport by moving world array content by value argument
def move_viewport(value):
    for e in world:
        e['pos']['x']+= value

# check if distance from player to screen border is lesser than minimum_distance_from_border and moves viewport if true
def check_distance_from_screen_border():
    player_x= get_player_x()
    distance_from_left_border= player_x
    distance_from_right_border= w- (player_x+ get_player_width())

    if distance_from_left_border<= minimum_distance_from_border:
        move_viewport(viewport_movement_value)
    if distance_from_right_border<= minimum_distance_from_border:
        move_viewport(-viewport_movement_value)

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
                # i have no idea why this globals() is necessary but if you remove it game will crash
                globals()['moves_left']-= 1
                event_queue.append({'action': 'mv', 'target': 'player', 'frames': 20, 'x': 12.4, 'y': 0})
            if event.key== pg.K_a:
                globals()['moves_left']-= 1
                event_queue.append({'action': 'mv', 'target': 'player', 'frames': 20, 'x': -12.4, 'y': 0})

# executes before render function
def prerender():
    check_keys() # check if some binded key has been pressed and do some action/event
    event_handler() # executes events from event_queue
    check_distance_from_screen_border() # check if player's distance to border is lesser than minimum_distance_from_border and if that is true moves viewport by moving world's content

# check if player still have some moves left
def check_if_player_lost_because_of_moves_count():
    b_player_event_in_queue= False
    # check if player movement still can change because of events from event_queue with target= 'player'
    for ev in event_queue:
        if ev['target']== 'player':
            b_player_event_in_queue= True

    if moves_left<= 0 and b_player_event_in_queue is False: return True
    else: return False

# game loop
while True:
    clock.tick(fps) # limits fps to value of fps variable
    prerender() # handling hotkeys, event_queue, etc.
    render() # draws objects and background

    # check if player lost the game
    if check_if_player_lost_because_of_moves_count():
        sys.exit()
