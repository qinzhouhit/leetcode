from heapq import *

class Solution:
    def kthSmallest(self, matrix, k):


        if not matrix or not matrix[0]:
            return None

        size=len(matrix)
        residue=k % size




