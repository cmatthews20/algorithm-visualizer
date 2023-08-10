import pygame
from utils import draw, generate_starting_list
from algorithms import bubble_sort, insertion_sort, selection_sort

pygame.init()

# Import after to initialize font
from draw_information import DrawInformation


def main():

    run = True # Variable for while loop
    clock = pygame.time.Clock() # regulates how quickly game will run
    
    # Variables to avoid hard coding multiple times
    n = 25
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
        
        clock.tick(30) # FPS
        
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
