'''keys: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problemsSolutions:Similar: T:S:'''from typing import Listclass Solution:    '''    At the end of the i-th day, we maintain cash: the maximum profit we     could have if we did not have a share of stock; and hold: the maximum     profit we could have if we owned a share of stock.    '''    # T: O(N); S: O(1)    def maxProfit(self, prices: List[int], fee: int) -> int:        # In day(0), cash(0) (stands for initial profit) is 0         # hold(0) is -prices[0]        cash, hold = 0, -prices[0]        for i in range(1, len(prices)): # from i-th day to (i+1)-th day            # we sell our stock            cash = max(cash, hold + prices[i] - fee)            # we buy a stock            hold = max(hold, cash - prices[i])        return cash