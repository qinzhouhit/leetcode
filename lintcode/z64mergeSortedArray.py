# lintcode
'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        i, j = m - 1, n - 1
        pos = m + n -1
        while i>=0 and j>=0:
            if A[i] > B[j]:
                A[pos] = A[i]
                pos -= 1
                i -= 1
            else:
                A[pos] = B[j]
                pos -= 1
                j -= 1

        while i >= 0:
            A[pos] = A[i]
            pos -= 1
            i -= 1
        while j >= 0:
            A[pos] = B[j]
            pos -= 1
            j -= 1


