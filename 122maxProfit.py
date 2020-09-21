'''
keys: as many as transactions you like
Solutions:
Similar: 121, 53
T:
S:
'''
from typing import List


class Solution:
    # TODO: calculate gains, see Huahua 121
    # T: O(N), S: O(1)
    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/39420/Three-lines-in-C%2B%2B-with-explanation
    # to be short: be a day trader when you can earn a penny
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                res += prices[i+1] - prices[i]
        return res

    # TODO: peak valley approach
    # buy at low valleys and sell at high peaks
    # T: O(N), S: O(1)
    def maxProfit1(self, prices: List[int]) -> int:
        valley, peak = prices[0], prices[0]
        maxprofit = 0; i = 0
        while i < len(prices)-1:
            while i < len(prices)-1 and prices[i+1] <= prices[i]:
                i += 1
            valley = prices[i]
            while i < len(prices)-1 and prices[i+1] >= prices[i]:
                i += 1
            peak = prices[i]
            maxprofit += peak - valley
        return maxprofit

