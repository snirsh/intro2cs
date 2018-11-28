import random

def swap(data,ind1,ind2):
    """swaps two items in a list"""
    data[ind1],data[ind2] = data[ind2],data[ind1]
    
def random_permute(data):
    """Permutes a list in-place randomly"""
    for i in range(len(data)-1):
        j = random.randrange(i,len(data))
        swap(data,i,j)

def find(item, data):
    """finds the index of a given item in a list"""
    for i in range(len(data)):
        if item==data[i]:
            return i
    return None
    
def find_max(data,num_elements):
    """finds the index of a maximal element in the list. 
    Inspects only the first num_elements elements""" 
    max_value = data[0]
    max_index = 0
    for i in range(1,num_elements):
        if data[i]>=max_value:
            max_value = data[i]
            max_index = i
    return max_index


def max_sort(data): 
    """sorts a list"""
    for num_el in range(len(data),1,-1):
        index_of_max = find_max(data,num_el)
        swap(data, index_of_max,num_el-1)
        
        
#sorting using a comparator function        
def find_max2(data,num_elements,cmp): 
    """finds the index of a maximal element in the list. 
    Inspects only the first num_elements elements
    uses a comparator function."""
    max_value = data[0]
    max_index = 0
    for i in range(1,num_elements):
        if cmp(data[i],max_value)>=0:                   
            max_value = data[i]
            max_index = i
    return max_index

def max_sort2(data,cmp):
    """sorts a list according to the given comparator.""" 
    for num_el in range(len(data),1,-1):
        index_of_max = find_max2(data,num_el,cmp)
        swap(data, index_of_max,num_el-1)

def binary_search(sorted_data,item):
    """returns the index of the item in the data, 
       if it was found. None otherwise"""
    bottom = 0 #The first cell in the suspected range
    top = len(sorted_data)-1 #the last cell
    
    while (top>=bottom):
        middle = (top+bottom)//2
        if sorted_data[middle] < item:
            bottom = middle+1
        elif sorted_data[middle] > item:
            top = middle-1
        else:
            return middle
    return None

def print_duplicates1(data):
    """prints all duplicate items in the list"""
    for i in range(1,len(data)):
        for j in range(i):
            if data[j]==data[i]:
                print(data[i])


def print_duplicates(data):
    """prints all duplicate items in the list"""
    #copy list and sort it.
    duplicate = list(data)
    quicksort(duplicate)
    
    #now, do the work:
    for i in range(len(data)-1):
        if(duplicate[i]==duplicate[i+1]):
            print(data[i])
    

def partition(data,start,end):
    """partitions the list (from start to end) around 
    a randomly selected pivot""" 
    #assumes start<end
    #select a random pivot, place it in the last index
    pivot_ind = random.randrange(start,end)
    pivot_val = data[pivot_ind]
    swap(data,pivot_ind,end-1)
    pivot_ind = end-1
    end -=1
    
    while(start<end):
        if(data[start])<pivot_val:
            start+=1
        elif(data[end-1])>=pivot_val:
            end-=1
        else: 
            swap(data,start,end-1)
            start+=1
            end-=1
    
    #swap pivot into place.
    swap(data,pivot_ind,start) 
    return start    

def quicksort(data):
    """quick-sorts a list """
    _quicksort_helper(data,0,len(data))
    
def _quicksort_helper(data,start,end):
    """A helper fucntion for quick-sort's recursion."""
    #start is the first index to sort, 
    #end is the index _after_ the last one
    if start<end-1:
        pivot_index = partition(data,start,end)
        _quicksort_helper(data,start,pivot_index)
        _quicksort_helper(data,pivot_index+1,end)

def reversed_comp(item1, item2):
    """a comparator function that 
    reverses the comparison order"""
    if item1>item2:
        return -1
    elif item2>item1:
        return 1
    else:
        return 0 

def comp_second(item1,item2):
    """a comparator function that 
    compares by the second value"""
    if item1[1]>item2[1]:
        return 1
    elif item2[1]>item1[1]:
        return -1
    else:
        return 0
