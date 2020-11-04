#Yield: Nó gần tương tự như return tuy nhiên return trả về 1 object còn yield sẽ trả về 1 generator
#Generator là 1 kiểu tương tự như interable tuy nhiên nó không có tính sử dụng, có nghĩa là nó sẽ bị đè giá trị

def change(lst):
	lstx = []
	for node in lst:
		lstx.append(node**2)
	return lstx
lst = [1,2,3]
k = change(lst)
print("vd hàm sài return")
for i in k:
	print(i)

def change2(lst):
	for node in lst:
		yield node**2
print('vd sài yield')
k2 = change2(lst)
for i in k2:
	print(i)

#Khi hàm có yield thì hàm sẽ chạy đến lệnh yield đầu tiên, sau đó sinh ra 1 generator. Sau đó chỉ đến khi gọi tiếp hàm thì nó mới trả ra
#giá trị tiếp.

def gen():
	yield 'Kteam'
	print('this is the second yield')
	yield 'Free education'
	print('this is the last yield')
	yield 'Long đẹp trai'
	print('Will not return anything')

#Dùng for để duyệt, ngoài ra còn có next:
m=[]
for val in gen():
	m.append(val)
	print(val) #gen() nó là 1 hàm nhưng có thể bóc tách từng giá trị nhờ việc nó có yield ở bên trong
print(m) #Giá trị của val sẽ là 3 cái yield ở trong hàm


#III. Phương thức send():
print("vd phương thức send")
def x():
	for i in range(4):
		x = yield i
		print("Let see",x)
g= x()
i1 = next(g)
print(i1)
g.send("Hjhj") #Nó thêm giá trị truyền vào cho biến x ở trong hàm
