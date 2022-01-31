# configuration is placed in settings.ini file that is read here
import configparser
import sys, os
filename= f"{os.path.dirname(os.path.realpath(__file__))}/settings.ini"
config= configparser.ConfigParser()
config.read(filename)

w, h= int(config.get("WINDOW", "w")), int(config.get("WINDOW", "h")) # size of window
minimum_distance_from_border= int(config.get("WINDOW", "minimum_distance_from_border")) # minimum distance of player to screen border before viewport moves
viewport_movement_value= int(config.get("WINDOW", "viewport_movement_value")) # value by which viewport moves when distance from screen border is lesser than minimum_distance_from_border. This value can be negative or positive depending on from which border distance is lesser than minimum_distance_from_border
font_family= config.get("FONT", "font_family") # font family that will be used for displaying every text
default_font_size= int(config.get("FONT", "default_font_size")) # default font size for interface etc.
counter_font_size= int(config.get("FONT", "counter_font_size")) # size of font that will be used to display how many moves left
scale= int(config.get("WINDOW", "scale")) # scale in which draw_world() will draw objects from world list
