#!/usr/bin/env python3

from helpers import window_helper
from helpers import image_helper
from puzzle_data import touch_puzzle_data
from puzzle_data import puzzle_data_collection

import os

g_piece_height_pixels = 62
g_piece_width_pixels = 90

class TouchPuzzleIntepreter:

    def __init__(self, touch_puzzle_data):
        self.touch_puzzle_data = touch_puzzle_data

    def interpret_touch_puzzle(self):
        image = window_helper.capture_game_window()
        image = image_helper.process_game_image(image)
        rectangles = image_helper.slice_rectangles(image, 
                                                   self.touch_puzzle_data.piece_height_pixels, 
                                                   self.touch_puzzle_data.piece_width_pixels)
        return rectangles

    def perform_move(self, 
                     source_piece_coord, 
                     dest_piece_coord):

        source_piece_x = source_piece_coord[0]
        source_piece_y = source_piece_coord[1]
        dest_piece_x = dest_piece_coord[0]
        dest_piece_y = dest_piece_coord[1]

        print(())
        window_helper.move_piece(source_piece_x * self.touch_puzzle_data.piece_width_pixels,
                                 source_piece_y * self.touch_puzzle_data.piece_height_pixels,
                                 dest_piece_x * self.touch_puzzle_data.piece_width_pixels,
                                 dest_piece_y * self.touch_puzzle_data.piece_height_pixels)

if __name__ == "__main__":
    resulting_path = "../../test/output"

    for f in os.listdir(resulting_path):
        os.remove(os.path.join(resulting_path, f))

    interpreter = TouchPuzzleIntepreter(puzzle_data_collection.puzzle_zero)
    rectangles = interpreter.interpret_touch_puzzle()
    interpreter.perform_move((0,0), (1,1))
    
    # image.save(os.path.join(resulting_path,"Image-TouchPuzzle.png"))
