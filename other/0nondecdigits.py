'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List

# https://www.geeksforgeeks.org/largest-number-smaller-equal-n-digits-non-decreasing-order/
'''Input  : n = 200
Output : 199
If the given number is 200, the largest 
number which is smaller or equal to it 
having digits in non decreasing order is
199.

Input  : n = 139
Output : 139'''


# Returns the required number 
def nondecdigits(n): 
  
    ''' loop to recursively check the numbers  
    less than or equal to given number'''
    for x in range(n, 0, -1): 
        no = x 
        prev_digit = float("inf") # or any number >= 10
  
        # Keep traversing digits from 
        # right to left. For every digit 
        # check if it is smaller than prev_dig 
        flag = True
        while (no != 0): 
            print (no % 10)
            if (prev_digit < no % 10): # use <= for monotonous increasing
                flag = False
                break # jump out of the for loop
              
            prev_digit = no % 10 # the digit from left end
            no //= 10
  
        # We found the required number 
        if (flag == True): 
            break
    return x 


def nondecdigits1(n): 




print (nondecdigits(200))








