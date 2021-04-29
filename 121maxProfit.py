'''
keys: at most one transaction
Solutions:
Similar: 53
T:
S:
'''

class Solution:
    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39038/Kadane's-Algorithm-Since-no-one-has-mentioned-about-this-so-far-%3A)-(In-case-if-interviewer-twists-the-input)
    # T: O(N), S: O(1)
    '''
    the logic is to calculate the difference (maxCur += prices[i] - prices[i-1]) 
    of the original array, and find a contiguous subarray giving maximum 
    profit. If the difference falls below 0, reset it to zero.
    Easy to see that we want continuous postive difference to accumulate to
    the maximum profit. The intermediate difference will be cancelled.
    '''
    def maxProfit1(self, prices):
        maxCur = 0; maxSoFar = 0
        for i in range(1, len(prices)):
            maxCur += prices[i] - prices[i-1]
            maxCur = max(0, maxCur) # choose the positive gains
            maxSoFar = max(maxCur, maxSoFar)
        return maxSoFar

    # T: O(N), S: O(1), the method to go
    # just keep updating the minimum price
    def maxProfit(self, prices):
        maxProfit, minPrice = 0, float('inf')
        for price in prices:
            minPrice = min(price, minPrice) # the min price appeared so far
            profit = price - minPrice
            maxProfit = max(maxProfit, profit)
        return maxProfit

    # self-made
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float("inf")
        maxProft = float("-inf")
        for price in prices:
            minPrice = min(minPrice, price)
            maxProft = max(maxProft, price - minPrice)
        return maxProft


    # brute force
    def maxProfit0(self, prices: List[int]) -> int:
        res = 0
        if not prices:
            return res
        n = len(prices)
        for i in range(n-1):
            lmin = min(prices[:i+1]) # including i
            lmax = max(prices[i+1:]) # from i+1
            res = max(res, lmax-lmin)
        return res
