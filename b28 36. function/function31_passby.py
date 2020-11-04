#Có 2 loại truyền đó là pass by reference và pass by value
#Pass by reference là đưa bản gốc còn value là đưa 1 bản sao

#Thông thường sẽ là pass by value: parameter k ảnh hưởng đến thằng gốc, tuy nhiên vd như interation thì sẽ có vấn đề 
#(như vd vòng for hôm bữa)

lst = [1,2,3]

def change(x):
	x[1] = 5
print(lst)
change(lst)
print(lst) #Kết quả 2 lần sẽ khác nhau

#II. Lệnh global: cho phép các biến trong hàm trở thành global:

def makeglobal():
	global k
	k = 5
makeglobal()
print("vd global",k)

#III. Hàm locals và globals
#Cho ta biết được các biến locals và globals có trong chương trình:

print(globals())
print(locals())