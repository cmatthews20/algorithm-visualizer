import random

def generate_starting_list(n, min_val ,max_val):

    lst = [] # Initialize empty list
    
    for _ in range(n):
        val = random.randint(min_val, max_val) # Num. in range (inclusive)
        
         # Adds random value to list. No need to shuffle since already random
        lst.append(val)
        
    return lst


lst = generate_starting_list(50,0,100)

print ("Unsorted array")
for i in range(len(lst)):
    print("%d" %lst[i],end=" ") 

def ascending_selection_sort(lst):
    
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):    
            if lst[min_index] > lst[j]:       
                min_index = j       
        lst[i], lst[min_index] = lst[min_index], lst[i]
        

def descending_selection_sort(lst):
    
    for i in range(len(lst) - 1, -1,-1):
        max_index = i
        for j in range(i - 1, -1, -1):    
            if lst[max_index] > lst[j]:       
                max_index = j       
        lst[i], lst[max_index] = lst[max_index], lst[i]




descending_selection_sort(lst)

print("\n")
print ("Sorted array")
for i in range(len(lst)):
    print("%d" %lst[i],end=" ") 
    