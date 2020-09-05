'''
keys:
Solutions:
Similar:
T:
S:
'''

from heapq import *

class Solution:
    def kthSmallest(self, matrix, k):

        # self-made, NlogN
        if not matrix or not matrix[0]:
            return None

        vals = [v for row in matrix for v in row ]
        vals.sort()
        # print (vals)
        return vals[k-1]




