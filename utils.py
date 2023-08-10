import pygame
import random


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
