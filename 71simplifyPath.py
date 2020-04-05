'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
	def simplifyPath(self, path):
		parts=[p for p in path.split("/")\
               if p!="." and p!=""]
		stack=[]
		for p in parts:
			if p=="..":
				if stack:
					stack.pop()
			else:
				stack.append(p)
		return "/"+"/".join(stack)

obj=Solution()
print(obj.simplifyPath("/a/./b/../../c/"))
