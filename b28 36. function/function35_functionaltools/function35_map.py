
#I. Hàm map:
# cú pháp: map(func, interable)

def func(x):
	x =x+1
	return x
lst = [1,2,3]

lst2 = list(map(func,lst)) #contructor list để đưa được giá trị mk cân cho thằng lst2
print("vd1",lst2)


#vd2: Dùng lambda:

lst3 = list(map(lambda x: x+1,lst))
print("vd lambda với map",lst3)

#vd3: truyền nhiều interable vào 1 lúc:

lstxx = [2,3,4]

lstvd3 = list(map(lambda x,y: x if x<y and x%2 == 0 else y,lst,lstxx))

print("vd nhiều interable cùng lúc",lstvd3)