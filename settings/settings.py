# TODO: load settings from json file

w, h= 1400, 800 # size of window
minimum_distance_from_border= 100 # minimum distance of player to screen border before viewport moves
viewport_movement_value= 400 # value by which viewport moves when distance from screen border is lesser than minimum_distance_from_border. This value can be negative or positive depending on from which border distance is lesser than minimum_distance_from_border
font_family= 'monospace' # font family that will be used for displaying every text
default_font_size= 16 # default font size for interface etc.
counter_font_size= 24 # size of font that will be used to display how many moves left
scale= 4 # scale in which draw_world() will draw objects from world list
