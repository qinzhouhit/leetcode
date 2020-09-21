'''
keys: DP, at most two transactions
Solutions:
Similar:
T:
S:
'''
from typing import List

class Solution:

    # TODO: one-pass simulation
    # S: O(1), four costs/ profits followed by four transactions
    def maxProfit1(self, prices: List[int]) -> int:
        t1_cost, t2_cost = float('inf'), float('inf')
        t1_profit, t2_profit = 0, 0

        for price in prices:
            # the maximum profit if only one transaction is allowed
            t1_cost = min(t1_cost, price)
            t1_profit = max(t1_profit, price - t1_cost)
            # reinvest the gained profit in the second transaction
            # taking into account the profit gained from the previous transaction #1
            # consider this as the cost of reinvestment
            # i.e., the more the t1_profit, the lower the t2_cost
            # then the higher the t2_profit
            t2_cost = min(t2_cost, price - t1_profit)
            t2_profit = max(t2_profit, price - t2_cost)

        return t2_profit




    # TODO: bidirectional dp, divide and conquer
    # T: O(N) for length of input sequence
    # S: O(N) for the two arrays we keep
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        left_min = prices[0]
        right_max = prices[-1]

        length = len(prices)
        # those left_profits and right_profits are for one transaction gain
        # left_profits[i] for prices[0:i+1], i.e., buying at 0
        left_profits = [0] * length
        # pad the right DP array with an additional zero for convenience.
        # right_profits[i] for prices[i:], i.e., selling at end
        # Have to pad extra 0 for case that only one transaction happened
        # i.e., left_profits[N-1] and empty right subsequence
        # if [0] * length, then in the last pass, change
        #  right_profits[i+1] to right_profits[i]
        right_profits = [0] * (length + 1) 

        # construct the bidirectional DP array
        for l in range(1, length):
            left_profits[l] = max(left_profits[l-1], prices[l] - left_min)
            left_min = min(left_min, prices[l])

            r = length - 1 - l
            right_profits[r] = max(right_profits[r+1], right_max - prices[r])
            right_max = max(right_max, prices[r])

        max_profit = 0
        for i in range(0, length):
            max_profit = max(max_profit, left_profits[i] + right_profits[i+1])

        return max_profit


sol = Solution()
print (sol.maxProfit([1,2,3,4,5]))
