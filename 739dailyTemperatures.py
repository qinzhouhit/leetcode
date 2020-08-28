'''keys: Solutions:Similar: T:S:'''from typing import Listclass Solution:    # next array    # T: O(N), N = len(T)    # S: O(W), W is the number of allowed values for T[i]    '''    Everytime a higher temperature is found, we update answer of the peak     one in the stack. If the day with higher temperature is not found, we     leave the ans to be the default 0.    '''    def dailyTemperatures1(self, T: List[int]) -> List[int]:        ans = [0] * len(T)        stack = []        for i, t in enumerate(T):            while stack and t > T[stack[-1]]:                cur = stack.pop()                ans[cur] = i - cur            stack.append(i) # t <= T[stack[-1]]            return ans                        # my naive, TLE    def dailyTemperatures(self, T: List[int]) -> List[int]:        res = []        for i in range(len(T)):            for j in range(i+1, len(T)):                ct = 0                if T[i] < T[j]:                    res.append(j - i)                    ct += 1                    break            if ct == 0 or i + 1 == len(T): # last day or no warmer day                res.append(0)        return res        