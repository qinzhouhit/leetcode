class Solution:
    def calculate(self, s: str) -> int:
        if s is None:
            return 0
        stack = []; num = 0; res = 0; sign = 1
        for str_ in s:
            if str_.isdigit():
                num = num*10 + int(str_)
            elif str_  in ["-", "+"]:
                res += sign*num
                num = 0
                sign = [-1, 1][str_ == "+"] # sign for the number after the sign
            elif str_ == "(":
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0 # reset the sign and result for the value in the parenthesis
            elif str_ == ")":
                res += sign*num
                res *= stack.pop() # stack.pop() is the sign before the parenthesis
                res += stack.pop() # stack.pop() now is the result calculated before the parenthesis
                num = 0
        return res + num*sign


obj = Solution()
print (obj.calculate("(1+(4+5+2)-3)+(6+8)"))

