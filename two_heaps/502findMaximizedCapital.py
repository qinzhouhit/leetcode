'''
keys: 
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# educative, io
	# you never push into the heap more than N times or pop from it more than k times
	# T: O(NlogN+KlogN), where ‘N’ is total number of projects and ‘K’ is number of projects
    # N = len(Profits), K = k
    # S: O(N), storing all the projects in the heaps.
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        min_cap, max_pro = [], []
        # insert all project capitals to a min-heap
        for idx, c in enumerate(Capital):
            heappush(min_cap, (c, idx))
            
        # find a total of 'k' best projects
        curCap = W
        for _ in range(k):
            # keep poping, i.e., one can invest 
            # # find all projects that can be selected within the available capital and 
            # insert them in a max-heap
            while min_cap and min_cap[0][0] <= curCap:
                capital, idx = heappop(min_cap)
                heappush(max_pro, (-Profits[idx],  idx))
            # not able to find any project that can be completed within the available capital
            if not max_pro:
                break
            # finish one at a time
            curCap += -heappop(max_pro)[0]
        return curCap

    # simplified
    def findMaximizedCapital1(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        min_cap, max_pro = [], []
        
        for idx, c in enumerate(Capital):
            heappush(min_cap, (c, Profits[idx]))
            
        curCap = W
        for _ in range(k):
            # keep poping, i.e., one can invest 
            while min_cap and min_cap[0][0] <= curCap:
                capital, profit = heappop(min_cap)
                heappush(max_pro, -profit)
            if not max_pro:
                break
            curCap += -heappop(max_pro)
        return curCap