'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    # stack; k[string]
    # T and S: O(maxK*n), maxK as max of k in s, n as length of s
    # k: the number outside of brackets
    def decodeString(self, s: str) -> str:
        
        res = ''; num = 0; stack = []
        for str_ in s:
            if str_.isdigit():
                num = int(str_) + 10*num 
            # dealing with things outside of [], i.e., existing
            # chars and numbers
            elif str_ == "[": 
                stack.append(res)
                stack.append(num)
                res = ''
                num = 0
            elif str_ == "]":
                num_pop = stack.pop()
                pre_str = stack.pop()
                res = pre_str + res * num_pop # key!!!
            else: # some char
                res += str_
        return res


    # self-made
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                sub = ''
                while stack[-1] != '[':
                    sub += stack.pop()
                # reverse the substring
                sub = sub[::-1]
                stack.pop() # pop "["
                num = ''
                while stack and stack[-1].isdigit():
                    num += stack.pop()
                num = int(num[::-1])
                stack += list(sub*num)
                
        return ''.join(stack)



    # >>> follow up
    '''
    如果数字也可以作为encoded string的一部分怎么做。如果数字在[]前，和原题一样视为次数，
    否则视为encoded string的一部分。
    比如: 3[a2b] -> a2ba2ba2b
    '''
    def decodeString1(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                sub = ''
                while stack[-1] != '[':
                    sub += stack.pop() # "b2a"
                # reverse the substring
                sub = sub[::-1] # "a2b"
                stack.pop() # pop "["
                num = ''
                while stack and stack[-1].isdigit():
                    num += stack.pop()
                num = int(num[::-1])
                stack += list(sub * num)
                
        return ''.join(stack)


obj = Solution()
print (obj.decodeString1("3[a2b]")) # 2[abc]3[cd]ef, 3[a2[c]]




