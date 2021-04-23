from helpers import content_grabber
from helpers import image_helper

class PuzzlePiece:
    def __init__(self, image):
        self.__image = image
        self.__position_x = 0
        self.__position_y = 0

    def get_image(self):
        return __image

    def get_position_x(self):
        return __position_x

    def get_position_y(self):
        return __position_y

class TouchPuzzleInterpreter:
    """ I """
    def __init__(self, image_2d_array):
        self.board = image_2d_array


    


