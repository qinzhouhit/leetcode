'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


'''
rand7() will get random 1 ~ 7
(rand7() - 1) * 7 + rand7() - 1 will get random 0 ~ 48
We discard 40 ~ 48, now we have rand40 equals to random 0 ~ 39.
We just need to return rand40 % 10 + 1 and we get random 1 ~ 10.

In 9/49 cases, we need to start over again.
In 40/49 cases, we call rand7() two times.

Overall, we need 49/40*2 = 2.45 calls of rand7() per rand10().

GNERALIZATION: https://leetcode.com/problems/implement-rand10-using-rand7/discuss/151567/C%2B%2BJavaPython-1.183-Call-of-rand7-Per-rand10
'''

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        rand40 = 40
        while rand40 >= 40:
            rand40 = (rand7() - 1) * 7 + rand7() - 1
        return rand40 % 10 + 1


   	# another one: using 1-6 to generate 1-10
   	def rand10(self):
     		rand30 = 30
     		while rand30 >= 30:
     			  rand30 = (rand6() - 1) * 6 + rand6() - 1
     		return rand30 % 10 + 1

    # another one, 1-5 to generate 1-7
    def rand7(self):
        rand24 = 24
        while rand24 >= 24:
            rand24 = (rand5() - 1) * 5 + rand5() - 1 # 0 - 24
        return rand24 % 4 + 1















