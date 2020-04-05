'''
keys:
Solutions:
Similar:
T:
S:
'''


# "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
class Solution:
    def lengthLongestPath(self, input):
        stack = [] # dummy head, but why
        max_ = 0
        if input is None:
            return 0
        attrs = input.split("\n")
        for attr in attrs:
            tab_ct = attr.count("\t")
            while tab_ct+1 < len(stack): # trace back to the parent lens
                stack.pop()
            len_ = stack[-1] + len(attr) - tab_ct + 1 # remove "\t\t..." add "\"
            stack.append(len_)
            if "." in attr:
                max_ = max(max_, len_ - 1) # - 1 because of dummy head
        return max_

a = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
obj = Solution()
print (obj.lengthLongestPath(a))
