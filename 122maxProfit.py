'''
keys:
Solutions:
Similar: 121, 53
T:
S:
'''
from typing import List


class Solution:
    # TODO: calculate gains, see Huahua 121
    # T: O(N), S: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                res += prices[i+1] - prices[i]
        return res

    # TODO: peak valley approach
    # T: O(N), S: O(1)
    def maxProfit1(self, prices: List[int]) -> int:
        valley, peak = prices[0], prices[0]
        maxprofit = 0; i = 0
        while i < len(prices)-1:
            while i < len(prices)-1 and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]
            while i < len(prices)-1 and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]
            maxprofit += peak - valley
        return maxprofit

