from utils import draw_list


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
                
                # Generator performs swap and goes back to where it was called from
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
