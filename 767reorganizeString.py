'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List
from collections import heapq

class Solution:
    # greedy with heap
    # T: O(NlogA)
    # S: O(A)
    def reorganizeString2(self, S):
        pq = [(-S.count(x), x) for x in set(S)]
        heapq.heapify(pg)
        if any(-ct > (len(s)+1)/2 for ct, x in pg):
            return ""

        res = []
        while len(pq) >= 2:
            ct1, ch1 = heapq.heappop(pq)
            ct2, ch2 = heapq.heappop(pq)
            #This code turns out to be superfluous, but explains what is happening
            #if not ans or ch1 != ans[-1]:
            #    ans.extend([ch1, ch2])
            #else:
            #    ans.extend([ch2, ch1])
            ans.extend([ch1, ch2])
            if ct1 + 1: 
                heapq.heappush(pq, (ct1 + 1, ch1))
            if ct2 + 1: 
                heapq.heappush(pq, (ct2 + 1, ch2))

        # second part is for single pair left in the heapq
        return "".join(ans) + (pq[0][1] if pq else '') 



    def reorganizeString1(self, S):
        '''
        T: O(A(N+logA)), A is the size of alphabet
        S: O(N)
        Put the least common letters at the odd indexes and 
        put the most common letters at the even indexes (both 
        from left to right in order of frequency)
        '''
        N = len(S)
        A = []
        for c, x in sorted((S.count(x), x) for x in set(S)):
            if c > (N+1)/2: return ""
            A.extend(c * x) # attention: A.extend("bb") -> A = ['b','b']
        ans = [None] * N
        # ans[::2]: all elements at even index, 0,2,4,6...
        # ans[1::2]: all elements at odd index, 1,3,5,7...
        print (A)
        print (A[N//2:])
        ans[::2] = A[N//2:]
        print (ans)
        ans[1::2] = A[:N//2]
        print (ans)
        return "".join(ans)
    
    
    # Time O(N): fill hash[] + find the letter + write results into char array
    # Space O(N + 26): result + hash[]
    def reorganizeString(self, S: str) -> str:
        hashmap = [0]*26
        for i in range(len(S)):
            hashmap[ord(S[i])-ord('a')] += 1
        
        max_ = max(hashmap)
        letter = hashmap.index(max_)
        
        # more than half of the S is one letter
        if max_ > (len(S)+1)//2: return ""
        
        idx = 0
        res = [''] * len(S)
        while hashmap[letter] > 0:
            res[idx] = chr(letter + ord('a'))  
            idx += 2
            hashmap[letter] -= 1
            
        for i in range(len(hashmap)):
            while hashmap[i] > 0:
                if idx >= len(res):
                    idx = 1
                res[idx] = chr(i + ord('a'))
                idx += 2
                hashmap[i] -= 1
        return "".join(res)
        
sol = Solution()
print (sol.reorganizeString1("aabbcdee"))
        
        
