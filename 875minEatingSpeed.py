'''keys: Solutions:Similar: T:S:'''from typing import Listclass Solution:    def minEatingSpeed(self, piles: List[int], H: int) -> int:                def helper(piles, speed):            res = 0            for p in piles:                if p % speed == 0: # finish it exactly                    res += p/speed                else:                    res += p//speed + 1            return res                        # initial slowest and fastest eating speed        l, r = 1, max(piles)        while l < r:            mi = int(l + (r - l)/2)            if helper(piles, mi) > H: # eat too slow                l = mi + 1            else:                r = mi        return l # not the mi                    