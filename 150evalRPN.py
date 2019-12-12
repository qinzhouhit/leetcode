class Solution:
    def evalRPN(self, tokens):
        if not any(tokens):
            return None
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in ["+", "-", "*", "/"]:
                stack.append(int(tokens[i]))
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                if tokens[i] == "+":
                    stack.append(int(val1) + int(val2))
                elif tokens[i] == "-":
                    stack.append(int(val1) - int(val2))
                elif tokens[i] == "*":
                    stack.append(int(val1) * int(val2))
                if tokens[i] == "/":
                    stack.append(int(int(val1) / int(val2)))
        return stack[0]

# obj = Solution()
# rpn = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# print (obj.evalRPN(rpn))

