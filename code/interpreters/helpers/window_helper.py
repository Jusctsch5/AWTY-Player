import pygetwindow
import time
import os
import pyautogui
import PIL
import pydirectinput

g_border_top_height_pixels = 4
g_border_bottom_height_pixels = 4

g_banner_height_pixels = 21
g_dosbox_header_height_pixels = 27

g_border_left_width_pixels = 4
g_border_right_width_pixels = 6

def convert_offset_to_window_offset(coordinate):
    coordinate = __add_banner_offset(coordinate)

    return coordinate

def __add_banner_offset(coordinate):
    new_coordinate = (coordinate[0], coordinate[1] + g_banner_height_pixels + g_dosbox_header_height_pixels)

    return new_coordinate

def __add_border_offset(coordinate, 
                        border_height_pixels = g_border_top_height_pixels, 
                        border_width_pixels = g_border_left_width_pixels):
    coordinate[0] + border_width_pixels
    coordinate[1] + border_height_pixels 

    return coordinate
    
def get_active_dos_window():
    titles = pygetwindow.getAllTitles()
    dosbox_title = None
    for title in titles:
        if "DOSBox 0.74" in title:
            dosbox_title = title

    if dosbox_title == None:
        raise IOError from None

    print(dosbox_title)

    window = pygetwindow.getWindowsWithTitle(dosbox_title)[0]
    if window == None:
        print("No Window!")
        raise IOError from None
    return window
    
def get_actual_window_coordinates(window):
    left = window.left+3
    top = window.top+2
    width = window.width-6
    height = window.height-5
    return left,top,width,height

def capture_game_window():
    window = get_active_dos_window()
    time.sleep(1)
    window.activate()
    time.sleep(1)

    left,top,width,height = get_actual_window_coordinates(window)
    image = pyautogui.screenshot(region=(left,
                                         top,
                                         width,
                                         height))

    return image

def move_piece(old_x, old_y, new_x, new_y):
    old_coordinate = convert_offset_to_window_offset((old_x, old_y))
    new_coordinate = convert_offset_to_window_offset((new_x, new_y))

    print("OLD: old_x:{}, old_y:{}. new_x:{}, new_y:{}".format(old_x, old_y, new_x, new_y))
    """
    old_x, old_y, new_x, new_y = old_x//2, old_y//2, new_x//2, new_y//2
    print("NEW: old_x:{}, old_y:{}. new_x:{}, new_y:{}".format(old_x, old_y, new_x, new_y))
    """

    window = get_active_dos_window()
    window.activate()

    left, top, width, height = get_actual_window_coordinates(window)
    pydirectinput.moveTo(left+20, top+50)
    pydirectinput.moveTo(left+20, top+50)
    pydirectinput.moveTo(left+20, top+50)
    pydirectinput.moveTo(left+20, top+50)

    time.sleep(.5)

    move_x = left + old_coordinate[0]
    move_y = top + old_coordinate[1]

    print("move_x:{}, move_y:{}".format(move_x, move_y))

    time.sleep(.5)
    pydirectinput.moveTo(move_x, move_y)
    time.sleep(.5)
    pydirectinput.mouseDown()
    time.sleep(.5)
    pydirectinput.mouseUp()

    move_x = left + new_coordinate[0]
    move_y = top + new_coordinate[1]

    print("move_x:{}, move_y:{}".format(move_x, move_y))

    time.sleep(.5)
    pydirectinput.moveTo(move_x, move_y)
    time.sleep(.5)
    pydirectinput.mouseDown()
    time.sleep(.5)
    pydirectinput.mouseUp()
    time.sleep(.5)

def move_test(start_position):

    print("Start X:Y" + str(start_position[0]) + ":" + str(start_position[1]))
    pydirectinput.moveTo(start_position[0]+100, start_position[1]+100)
    time.sleep(.5)

    while 1:
        pydirectinput.moveRel(0, 100)
        pydirectinput.mouseDown()
        time.sleep(1)
        pydirectinput.mouseUp()
        time.sleep(1)

        pydirectinput.moveRel(100, 0)
        pydirectinput.mouseDown()
        time.sleep(1)
        pydirectinput.mouseUp()
        time.sleep(1)

        pydirectinput.moveRel(0, -100)
        pydirectinput.mouseDown()
        time.sleep(1)
        pydirectinput.mouseUp()
        time.sleep(1)

        pydirectinput.moveRel(-100, 0)
        pydirectinput.mouseDown()
        time.sleep(1)
        pydirectinput.mouseUp()
        time.sleep(1)

        print("Loop")
        time.sleep(1)

if __name__ == "__main__":
    window = get_active_dos_window()
    left, top, width, height = get_actual_window_coordinates(window)

    window.activate()
    
    move_test((left, top))