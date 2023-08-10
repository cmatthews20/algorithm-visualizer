import pygame
import math


class DrawInformation:
    """
    Don't want to use global variables.
    Instead, this Class for global values to be accessed.
    """
    
    #RGB color codes
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    BLUE = 0, 0, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    
    GREY0 = 128, 128, 128
    GREY1 = 160, 160, 160
    GREY2 = 160, 160, 160
    
    BACKGROUND_COLOR = WHITE

    GRADIENT = [
        GREY0,
        GREY1,
        GREY2
    ] 

    # Font needed whenever you want to type something
    FONT = pygame.font.SysFont('arial', 20)
    LARGE_FONT = pygame.font.SysFont('arial', 30)
    
    SIDE_PAD = 100 # Total number of pixels (left + right) as sidebar padding
    TOP_PAD = 150 # Padding for controls and text at top of window


    def __init__(self, width, height, lst):
        '''

        Parameters
        ----------
        width : int
            Pixel width of game window
        height : int
            Pixel height of game window
        lst : TYPE
            DESCRIPTION.

        Returns
        -------
        None.
        '''

        self.width = width
        self.height = height
        
        # Need to setup pygame window/screen to draw everything on
        # Needs to be accesible everywhere
        # Pass width and height as tuple to set_mode
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Cole's Sorting Algorithm Visualizer")


    def set_list(self, lst):
        '''
        
        Parameters
        ----------
        lst : TYPE
            DESCRIPTION.

        Returns
        -------
        None.
        '''
        self.lst = lst
        self.max_val = max(lst) # Biggest list value
        self.min_val = min(lst) # Smallest list value
        
        # Determines width of the visual bars to be sorted
        # Needs to be floor rounded; can't draw fractional amounts
        # Use floor to not go above TOP_PAD
        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        
        # Height of the blocks depend on largest and smallest numbers in list
        # Determines true pixel hight based on list attributes
        # Determines total 'drawable area'
        self.block_height = math.floor(
            (self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        
        # Where the drawing starts (as an x-coordinate)
        self.start_x = self.SIDE_PAD // 2 # Still need whole number
