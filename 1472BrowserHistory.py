'''
keys: browse history
Solutions:
Similar:
T:
S:
'''
from typing import List


class BrowserHistory:
# https://leetcode.com/problems/design-browser-history/discuss/674324/Python-Easy-Solution-with-Explanation
	# S: O(n), n as the most urls we have
    def __init__(self, homepage: str):
        self.pages = [homepage]
        self.cur = 0

    # O(n)
    def visit(self, url: str) -> None:
    	# when visiting a new url, you can no longer forward
        # remove all history for forwards, i.e., forward till the current idx
        while len(self.pages)-1 != self.cur:
        	self.pages.pop()
        self.cur += 1
        self.pages.append(url)
      
    # T: O(1)
    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.pages[self.cur]

    # T: O(1)
    def forward(self, steps: int) -> str:
        self.cur = min(len(self.pages)-1, self.cur+steps)
        return self.pages[self.cur]

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)