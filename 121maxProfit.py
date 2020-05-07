'''
keys:
Solutions:
Similar: 53
T:
S:
'''

class Solution:
    def maxProfit1(self, prices):
        maxCur = 0; maxSoFar = 0
        for i in range(1, len(prices)):
            maxCur += prices[i] - prices[i-1]
            maxCur = max(0, maxCur) # choose the positive gains
            maxSoFar = max(maxCur, maxSoFar)
        return maxSoFar

    # T: O(N), S: O(1)
    def maxProfit(self, prices):
        maxProfit, minPrice = 0, float('inf')
        for price in prices:
            minPrice = min(price, minPrice)
            profit = price - minPrice
            maxProfit = max(maxProfit, profit)
        return maxProfit

