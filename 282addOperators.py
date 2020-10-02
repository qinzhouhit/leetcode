'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List

class Solution:
    # intuitive
    # https://leetcode.com/problems/expression-add-operators/discuss/71895/Java-Standard-Backtrace-AC-Solutoin-short-and-clear
    # T: O(N*4^N) for 4 recursive paths, N for length of num
    # S: O(N)
    def addOperators1(self, num: str, target: int) -> List[str]:
        self.ans = []
        if not num or len(num) == 0: return self.ans
        self.helper("", num, target, 0, 0, 0)
        return self.ans
    
    def helper(self, path, num, target, pos, val, multed): # multed is prev_operand
        if pos == len(num):
            if val == target:
                self.ans.append(path)
                return
        
        for i in range(pos, len(num)): # to divide the string into operands
            if i != pos and num[pos] == '0': # avoiding "05"-like cases, run ("105", 5)
                break
            cur = int(num[pos:i+1]) # operand
            if pos == 0: # first "number"
                self.helper(path + str(cur), num, target, i+1, cur, cur)
            else:
                self.helper(path + "+" + str(cur), num, target, i+1, val+cur, cur)
                self.helper(path + "-" + str(cur), num, target, i+1, val-cur, -cur)
                self.helper(path + "*" + str(cur), num, target, i+1, \
                            val - multed + multed * cur, multed * cur )
                
    
    
    
    # official
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []
        n = len(num)
        def dfs(idx, prev_operand, cur_operand, val, string):
        	# Done processing all the digits in num
            if idx == n:
                # If the final value == target expected AND
                # no operand is left unprocessed
                if val == target and cur_operand == 0:
                
                    ans.append("".join(string[1:]))
                return

            # Extending the current operand by one digit
            cur_operand = cur_operand*10 + int(num[idx])
            str_op = str(cur_operand)
            
            # To avoid cases where we have 1 + 05 or 1 * 05 since 05 
            # won't be a valid operand. Hence this check
            if cur_operand > 0:
                # no operator recursion
                dfs(idx+1, prev_operand, cur_operand, val, string)
            # addtion recursion
            string.append("+"); string.append(str_op)
            dfs(idx+1, -cur_operand, 0, val-cur_operand, string)
            string.pop(); string.pop()
            # multiplication
            string.append("*"); string.append(str_op)
            dfs(idx+1, cur_operand*prev_operand, 0, val-prev_operand\
                + (cur_operand*prev_operand), string)
            string.pop(); string.pop()
        dfs(0, 0, 0, 0, [])
        return ans
            
            
            
            
            
            
            
            
            
            
            
        
        
