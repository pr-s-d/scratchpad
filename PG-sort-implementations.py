# -*- coding: utf-8 -*-

def sort_binary(a_list):
    """
    Parameters
    ----------
    a_list : List of sortable values (e.g., integers)
        This list is unsorted. Approach is to take the first item as 
        a 'pivot value' and split the list into a 'left' and 'right' half of
        lower and higher values, and then recursively sort that list, until
        the list is <=2 long

    Returns
    -------
    sorted_list : Sorted list
        The result of the 'binary sort' algorithm.

    """
    sorted_list = [] #hoped for output
    
    #return the list once it's 0 or 1 item long
    if len(a_list) < 2:
        return a_list
    #otherwise make the less and more lists
    else:
        pivot = a_list[0] #set pivot value
        less = [] #less than pivot
        more = [] #greater than pivot
 
        for val in a_list[1:]:
            if val <= pivot:
                less.append(val)
            else:
                more.append(val)
     
        left = sort_binary(less)
        right = sort_binary(more)
    
        sorted_list.extend(left)
        sorted_list.append(pivot)
        sorted_list.extend(right)
        return sorted_list
    

def merge_sort(a_list):
    """

    Parameters
    ----------
    a_list : list of sortable values (e.g., integers)
        The list is unsorted. The function sorts the list in ascending order
        using a mergesort algorithm

    Returns
    -------
    sorted_list : Sorted list
        The result of the mergesort algorithm

    """

    sorted_list = [] #initialize output
    
    # return the list if it's 0 or 1 long
    if len(a_list) < 2:
        return a_list
    #otherwise, split and merge the lists in left / right branches
    else:
        midpt = len(a_list) // 2 #dividing point
        left = merge_sort(a_list[:midpt])  #recursive call to sort
        right = merge_sort(a_list[midpt:]) #recursive call to sort
        
        #now make the merged sorted list, knowing that left and right are sorted
        while len(left) < 0 and len(right) < 0:
            if left[0] < right[0]:
                sorted_list.append(left[0])
                del left[0]
            else:
                sorted_list.append(right[0])
                del right[0]
        
        sorted_list.extend(left)
        sorted_list.extend(right)
        return sorted_list
    