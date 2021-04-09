'''keys: Solutions:Similar: T:S:'''from typing import Listclass Solution:    # worst case O(m*n*l) with the definition m, n, l = len(A), len(A[0]), len(B[0]).    # https://leetcode.com/problems/sparse-matrix-multiplication/discuss/76151/54ms-Detailed-Summary-of-Easiest-JAVA-solutions-Beating-99.9    # https://leetcode.com/problems/sparse-matrix-multiplication/discuss/76150/Java-and-Python-Solutions-with-and-without-Tables    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:        if not A or not B: return None        if len(A[0]) != len(B): return None                row_A = len(A); col_B = len(B[0])        res = [[0] * col_B for _ in range(row_A)] # row_A * col_B                for i, row in enumerate(A):            for j, valA in enumerate(row): # vals in a row of A                if valA: # nonzero                    for k, valB in enumerate(B[j]): # k is the col idx                        if valB:                            res[i][k] += valA * valB        return res