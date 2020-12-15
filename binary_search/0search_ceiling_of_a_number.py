'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


'''
Given an array of numbers sorted in an ascending order, find the ceiling of a given 
number ‘key’. The ceiling of the ‘key’ will be the smallest element in the given array 
greater than or equal to the ‘key’.

Write a function to return the index of the ceiling of the ‘key’. If there isn’t any 
ceiling return -1.
'''

def search_ceiling_of_a_number(arr, key):
    l, r = 0, len(arr) - 1 
    while l <= r: 
        mid = l + (r-l)//2 
        if arr[mid] == key: 
            return mid 
        elif key > arr[mid]: 
            l = mid + 1 
        else: 
            r = mid - 1 
    # since the loop is running until 'l <= r', so at the end of the while loop, 'l == r+1' 
    # we are not able to find the element in the given array, so the next big number will 
    # be arr[start] 
    return l if l < len(arr) else -1


# similar one 
'''
Given an array of numbers sorted in ascending order, find the floor of a given number ‘key’.
The floor of the ‘key’ will be the biggest element in the given array smaller than or 
equal to the ‘key’
'''

def search_floor_of_a_number(arr, key):
    l, r = 0, len(arr) - 1 
    while l <= r: 
        mid = l + (r-l)//2 
        if arr[mid] == key: 
            return mid 
        elif key > arr[mid]: 
            l = mid + 1 
        else: 
            r = mid - 1 
    return r if r >= 0 else -1


















