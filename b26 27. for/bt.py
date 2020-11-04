lst = [[1, 2, 3], [4, 5, 6]]
# node = 0
# for a in lst:
# 	a[0] = None
# 	lst[node] = a
# 	node += 1
# 	print(a)
# print(lst)
for l in lst:
	l[0] = None
print(lst)  #Có thể là tạo ra biến l cũng trỏ về thằng lst[0] nên l thay đổi thì lst[0] cũng thay đổi

lst = [1, 2, 3]
for value in lst:
	value += 1
	print(value)
print(lst)