'''keys: Solutions:Similar: T: O(nlogn)S: O(n), n = len(sticks)'''from typing import Listimport heapq'''The earlier combined sticks are added more times, so if we want to minimize cost, we will want to combine the smaller ones as early as possible.'''class Solution:    def connectSticks(self, sticks: List[int]) -> int:        heapq.heapify(sticks)        res = 0        while len(sticks) > 1:            x, y = heapq.heappop(sticks), heapq.heappop(sticks)            res += x + y            heapq.heappush(sticks, x + y)        return res                                    # if no modification to the input    def connectSticks1(self, sticks: List[int]) -> int:        h = []        for s in sticks:            heapq.heappush(h, s)        sum = 0        while len(h) > 1:            two = heapq.heappop(h) + heapq.heappop(h)            sum += two            heapq.heappush(h, two)        return sum    