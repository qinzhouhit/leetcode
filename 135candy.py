'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
    # TODO: single pass with constant space
    # T: O(n); S: O(1)
    # https://leetcode.com/problems/candy/discuss/42770/One-pass-constant-space-Java-solution
    # http://www.allenlipeng47.com/blog/index.php/2016/07/21/candy/
    def candy3(self, ratings: List[int]) -> int:
        len_ = len(ratings)
        pre, total = 1, 1
        countDown = 0
        for i in range(1, len_):
            if ratings[i] >= ratings[i-1]:
                if countDown > 0:
                    total += countDown * (countDown + 1) / 2
                    if countDown >= pre:
                        total += countDown - pre + 1
                    pre = 1
                    countDown = 0
                pre = 1 if ratings[i] == ratings[i-1] else pre + 1
                total += pre
            else:
                countDown += 1
        if countDown > 0:
            total += countDown * (countDown + 1) / 2
            if countDown >= pre:
                total += countDown - pre + 1
        return int(total)





    # TODO: using one array
    # T: O(n); S: O(n)
    def candy2(self, ratings: List[int]) -> int:
        len_ = len(ratings)
        candies = [1]*len_
        for i in range(1, len_):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        res = candies[-1]
        for i in range(len_-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)
            res += candies[i]
        return res


    # TODO: two arrays
    # T: O(n); S: O(n)
    def candy1(self, ratings: List[int]) -> int:
        res = 0; len_ = len(ratings)
        left2right = [1]*len_
        right2left = [1]*len_
        for i in range(1, len_):
            if ratings[i] > ratings[i-1]:
                left2right[i] = left2right[i-1] + 1
        for i in range(len_-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right2left[i] = right2left[i+1] + 1
        for i in range(len_):
            res += max(left2right[i], right2left[i])
        return res


    # TODO: brutal force, TLE
    # T: O(n^2); S: O(n)
    def candy(self, ratings: List[int]) -> int:
        len_ = len(ratings)
        candies = [1]*len_
        flag = True
        while flag:
            for i in range(len_):
                if i != len_-1 and ratings[i] > ratings[i+1] \
                        and candies[i] <= candies[i+1]:
                    candies[i] = candies[i+1] + 1
                    flag = True
                if i > 0 and ratings[i] > ratings[i-1] and \
                    candies[i] <= candies[i-1]:
                    candies[i] = candies[i-1] + 1
                    flag = True
        return sum(candies)

