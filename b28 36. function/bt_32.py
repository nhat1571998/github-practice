def tinh(x):
	k = x**3 + 2*x**2 - 4*x+1
	return k
def func(lst):
	l1,l2 = [],[]
	for node in lst:
		if(node[1] == tinh(node[0])):
			l1.append(node)
		else:
			l2.append(node)
	return l1,l2
lst = [(1,2),(3,4),(1,0),(2,9)]
l1,l2 = func(lst)
print("List thuộc đồ thị:",l1)
print("List không thuộc đồ thị",l2)