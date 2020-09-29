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
    def decodeString(self, s: str) -> str:
        
        res = ''; num = 0; stack = []
        for str_ in s:
            if str_.isdigit():
                num = int(str_) + 10*num
            elif str_ == "[":
                stack.append(res)
                stack.append(num)
                res = ''
                num = 0
            elif str_ == "]":
                num_pop = stack.pop()
                pre_str = stack.pop()
                res = pre_str + res * num_pop
            else: # some char
                res += str_
        return res

obj = Solution()
print (obj.decodeString("2[abc]3[cd]ef"))




