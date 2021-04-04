'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List







class Solution:


    ##### concise
    def lastRemaining(self, n):
        arr = range(1, n+1)
        while len(arr) > 1:
            arr = arr[1::2][::-1]
        return arr[0]


    # https://leetcode.com/problems/elimination-game/discuss/87119/JAVA%3A-Easiest-solution-O(logN)-with-explanation
    # S: O(1), T: O(logn)
    # this is hard to think of...
    def lastRemaining(self, n: int) -> int:
        remaining = n
        startLeft = True # indicating the direction of deleting
        step = 1
        head = 1 # the first numebr
        while remaining > 1:
            # remaining % 2 means 
            if startLeft or remaining % 2:
                head += step
            remaining //= 2
            step *= 2
            startLeft = not startLeft # start from right
        return head


    #####
    def lastRemaining(self, n):

        def helper(n, startLeft): # startLeft means starting from left
            if n == 1: # only one element left
                return 1
    # if started from left side the odd elements will be removed, the only remaining ones will the the even i.e.
    #       [1 2 3 4 5 6 7 8 9]==>[2 4 6 8]==2*[1 2 3 4]
            if startLeft:
                return 2 * helper(n // 2, 0)
    # same as left side the odd elements will be removed
            elif n % 2 == 1:
                return 2 * helper(n // 2, 1)
    # even elements will be removed and the only left ones will be 
    # [1 2 3 4 5 6 ] == [1 3 5] == 2*[1 2 3] - 1
            else: # n % 2 == 0
                return 2 * helper(n // 2, 1) - 1
        return helper(n, 1)


    


