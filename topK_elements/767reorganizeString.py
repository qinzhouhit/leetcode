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
    # educative.io version
    def reorganizeString3(self, S):
        ct = Counter(S)
        h = []
        for c, freq in ct.items():
            if freq > (len(S) + 1) / 2:
                return ""
            heappush(h, (-freq, c))
        prevChar, prevFreq = None, 0
        res = []
        while h:
            freq, char = heappop(h)
            if prevChar and prevFreq < 0:
                heappush(h, (prevFreq, prevChar))
            # append the cur char to the res and decrement the freq
            res.append(char)
            prevChar = char
            prevFreq = freq + 1
        # dont need this line
        # return "".join(res) if len(res) == len(S) else ""
        return "".join(res) 


    # greedy with heap
    # T: O(NlogA), A is the size of the alphabet
    # S: O(A)
    def reorganizeString2(self, S):
        pq = [(-S.count(x), x) for x in set(S)]
        heapq.heapify(pg)
        if any(-ct > (len(s)+1)/2 for ct, x in pg):
            return ""

        ans = []
        while len(pq) >= 2:
            freq1, ch1 = heapq.heappop(pq)
            freq2, ch2 = heapq.heappop(pq)
            #This code turns out to be superfluous, but explains what is happening
            #if not ans or ch1 != ans[-1]:
            #    ans.extend([ch1, ch2])
            #else:
            #    ans.extend([ch2, ch1])
            ans.extend([ch1, ch2])
            if freq1 + 1: # notice the freq is negative here...
                heapq.heappush(pq, (freq1 + 1, ch1))
            if freq2 + 1: 
                heapq.heappush(pq, (freq2 + 1, ch2))

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
        
        
