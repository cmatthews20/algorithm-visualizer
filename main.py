# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 12:59:11 2022

@author: Cole
MY NOTES:
    - Change and organize text at top
    - Redo docstrings
"""

import random # For generating starting list
import pygame
import math

pygame.init()

# Don't want to use global variables
# Class for global values to be accessed
class DrawInformation:
    
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


def generate_starting_list(n, min_val ,max_val):
    '''
    Generates starting list within list parameters

    Parameters
    ----------
    n : TYPE
        Number of elements in starting list
    min_val : TYPE
        Minimum possible value
    max_val : TYPE
        Maximum possible value

    Returns
    -------
    lst : Array
        The newly generated array
    '''
    lst = [] # Initialize empty list
    
    for _ in range(n):
        val = random.randint(min_val, max_val) # Num. in range (inclusive)
        
         # Adds random value to list. No need to shuffle since already random
        lst.append(val)
        
    return lst


def draw_list(draw_info, color_positions = {}, clear_background = False):
    '''
    Need to look at every element in list, determine hight of that element,
    x-coord of the element, draw the rectangle to represent it, 
    and make sure all rectangles are a slightly different color (so we can 
    actually see them)

    Parameters
    ----------
    draw_info : TYPE
        DESCRIPTION.
    color_positions : Dictionary
        DESRIPTION
    clear_background : Bool
        DESCRIPTION
        
    Returns
    -------
    None.
    '''
    lst = draw_info.lst # Avoid writing draw_info.lst a bunch of times
    
    if clear_background:
        clear_rect = (
            draw_info.SIDE_PAD//2, 
            draw_info.TOP_PAD, 
            draw_info.width - draw_info.SIDE_PAD, 
            draw_info.height - draw_info.TOP_PAD)
        
        pygame.draw.rect(
            draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)
    
    for i, val in enumerate(lst): # Index and value of every element in list

        x = draw_info.start_x + i * draw_info.block_width
        
        # Calculate and normalize height values
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height
        
        # Different %3 to give different color
        color = draw_info.GRADIENT[i % 3] 
        
        if i in color_positions:
            color = color_positions[i]
        
        # Make the rectangle/bar. Actual bar will extend past bottom screen 
        # limit but we cant see it so its okay
        pygame.draw.rect(
            draw_info.window, color, 
            (x, y, draw_info.block_width, draw_info.height))
        
    if clear_background:
        pygame.display.update()


def draw(draw_info, algo_name, ascending):
    '''
    Actually draws the list. Fills the screen with background color. 
    Updates display. Draws the list
    In Pygame, you have to draw stuff, and then update display to apply it

    Parameters
    ----------
    draw_info : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    # Set bacground color
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    
    # Render text for sorting and control commands
    title = draw_info.LARGE_FONT.render( # Use fstring with conditional inside
        f"{algo_name} - {'Ascending' if ascending else 'Descending'}",
        1, draw_info.BLUE)
    
    controls = draw_info.FONT.render(
        "R - Randomize | SPACE - Start Sorting | A - Ascending | D - Descending", 
        1, draw_info.BLACK)
    
    sorting = draw_info.FONT.render(
        "B - Bubble Sort | I - Insertion Sort | S - Selection Sort", 
        1, draw_info.BLACK)
 
    
    # x_coord to align texts with center of screen
    title_center = draw_info.width/2 - title.get_width()/2
    controls_center = draw_info.width/2 - controls.get_width()/2
    sorting_center = draw_info.width/2 - sorting.get_width()/2
    
    # Place text in center of screen
    draw_info.window.blit(title, (title_center, 5))
    draw_info.window.blit(controls, (controls_center, 45))
    draw_info.window.blit(sorting, (sorting_center, 75))

    
    draw_list(draw_info)
    pygame.display.update()


def bubble_sort(draw_info, ascending = True):
    lst = draw_info.lst
    
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]
            
            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j] # Single line value swap
                draw_list(
                    draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True)
                
                # Generator (similar to iterator for for loop)
                # Performs swap and goes back to where it was called from
                # Essentialy 'stores' where the loop left off and goes back to 
                # where function was called
                yield True 
    return lst


def insertion_sort(draw_info, ascending = True):
    lst = draw_info.lst
    
    for i in range(1, len(lst)):
        current = lst[i]
        
        while True:
            ascending_sort = i > 0 and lst[i - 1] > current and ascending
            descending_sort = i > 0 and lst[i - 1] < current and not ascending
            
            if not ascending_sort and not descending_sort:
                break
            
            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] = current
            
            draw_list(draw_info, {i - 1: draw_info.GREEN, i: draw_info.RED}, True)
            
            yield True
            
    return lst


def selection_sort(draw_info, ascending = True):
    lst = draw_info.lst
    
    if ascending:
        for i in range(len(lst)):
            min_index = i
            for j in range(i + 1, len(lst)):    
                if lst[min_index] > lst[j]:       
                    min_index = j       
            lst[i], lst[min_index] = lst[min_index], lst[i]
            draw_list(draw_info, {i: draw_info.GREEN, min_index: draw_info.RED}, True)
            yield True
    
    else:
        for i in range(len(lst) - 1, -1,-1):
            max_index = i
            for j in range(i - 1, -1, -1):    
                if lst[max_index] > lst[j]:       
                    max_index = j       
            lst[i], lst[max_index] = lst[max_index], lst[i]
            draw_list(draw_info, {i: draw_info.GREEN, max_index: draw_info.RED}, True)
            yield True
    
    return lst


def main():

    run = True # Variable for while loop
    clock = pygame.time.Clock() # regulates how quickly game will run
    
    # Variables to avoid hard coding multiple times
    n = 100
    min_val= 0
    max_val = 100
    
    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(800, 600, lst)
    draw_info.set_list(lst)
    sorting = False
    ascending = True
    algorithm = bubble_sort
    algorithm_name = "Bubble Sort"
    algorithm_generator = None
    
    
    # Pygame event loop. Without a loop, game will end automatically
    while run:
        
        clock.tick(5) # FPS
        
        if sorting:
            try:
                next(algorithm_generator)
                
            # When exception is thrown, we know it is done sorting
            except StopIteration: 
                sorting = False # Accept this and move on
        
        else:
            draw(draw_info, algorithm_name, ascending)
       
        
        pygame.display.update() # Updates display
        
        # event.get() returns list of all events that have occured since last loop
        for event in pygame.event.get():  
            
            if event.type == pygame.QUIT: # Manual handle of 'X' button
                run = False   
                
            if event.type != pygame.KEYDOWN:
                continue
            
            if event.key == pygame.K_r:
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            
            
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                algorithm_generator = algorithm(draw_info, ascending)
                
            elif event.key == pygame.K_a and not sorting:
                ascending = True
        
            elif event.key == pygame.K_d and not sorting:
                ascending = False
                
            elif event.key == pygame.K_i and not sorting:
                algorithm = insertion_sort
                algorithm_name = "Insertion Sort"
                
            elif event.key == pygame.K_b and not sorting:
                algorithm = bubble_sort
                algorithm_name = "Bubble Sort" 
                
            elif event.key == pygame.K_s and not sorting:
                algorithm = selection_sort
                algorithm_name = "Selection Sort" 

    pygame.quit()

if __name__ == "__main__": # Makes sure module is running 
    main()
