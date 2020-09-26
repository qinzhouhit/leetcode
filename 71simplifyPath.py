'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    # O(N) for S and T
    # "." can be ignored, "" means we have "//"
	def simplifyPath(self, path):
        # "//".split("/") = ['', '', '']
		parts = [p for p in path.split("/") if p != "." and p != ""]
		stack = []
		for p in parts:
			if p == "..":
				if stack:
					stack.pop()
			else:
				stack.append(p)
		return "/"+"/".join(stack)

obj=Solution()
print(obj.simplifyPath("/a/./b/../../c/"))
