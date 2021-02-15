a = [3,3,10,7,4,3,0]
stack = []
for v in a:
	if v % 2:
		stack.append(v)
		print (len(stack))
	else:
		val = stack.pop()
		if val > v:
			stack.append(v)
			print (len(stack))