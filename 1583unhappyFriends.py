'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# O(n^2) by using set
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        
        dd = {}
        
        for u1, u2 in pairs: # dd records the prefered candidates over paired
            dd[u1] = set( preferences[u1][:preferences[u1].index(u2)] )
            dd[u2] = set( preferences[u2][:preferences[u2].index(u1)] )
        
        ans = 0
            
        for u1 in dd:
            for candidate in dd[u1]:
                if u1 in dd[candidate]:
                    ans += 1
                    break
        
        return ans


    # wrong
    def unhappyFriends1(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        if not preferences or not pairs:
            return 0
        
        res = 0
        for x, y in pairs:
            best_x = preferences[x][0]
            best_y = preferences[y][0]
            # if best_x == y and best_y == x:
            #     continue
            if best_x != y:
                u_s = preferences[x][:preferences[x].index(y)]
                for u in u_s: 
                    if preferences[u].index(x) < len(preferences[u])-1:
                        res += 1
            if best_y != x:
                u_s = preferences[y][:preferences[y].index(x)]
                for u in u_s: 
                    if preferences[u].index(y) < len(preferences[u])-1:
                        res += 1
        return res-1
