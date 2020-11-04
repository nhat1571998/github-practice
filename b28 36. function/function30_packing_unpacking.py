
#I. Unpacking arguments vs *:
#VD như là có 1 hàm n tham số đều thuộc 1 list thì chả nhẽ phải tách list rồi nhét vào từng tham số
#=> Chỉ cần unpack là xong: List, chuỗi, tuple, dict, set

#Lưu ý: unpack thường được sử dụng cho các hàm k có default argument => positional argument

#Lỡ mà còn các biến khác thì sử dụng theo cú pháp:    kteam(*('a', 'b', 'c'), 'd')
lst=["Haha",1,2,3] #Sẽ báo lỗi nếu tham số truyền vào nhiều hơn số parameter
def vd1(a,b,c,d):
	print("Ví dụ 1:",a,b,c,d)
vd1(*lst)

#II. Packing arguments vs *:
#vd như muốn truyền nhiều biến a vào cùng 1 lúc thì thay vì ngồi gõ từng lần thì ta có thể sử dụng thằng này:
def x(*a):
	print(a)
	print(type(a))

x(1,2,3,4,5)

def x2(*a,b):
	print(a,b)

x2(1,2,3,b=4) # truyền tham số sau 1 packing argument thì cần dùng password argument

#Không được phép để 2 parameter có cùng kiểu packing argument trong cùng 1 hàm

#III. Unpacking vs **: Dùng cho dict do dict có 2 tham số.

dic = {"name":"nhat","age":"22"}
def ix(name,age):
	print(name,age)
ix(*dic) #Kết quả: name age vì nó k thể lấy được val
print("------------------")
ix(**dic) #Chú ý: vì làm ntn thì được hiểu là kiểu password argument nên parameter bắt buộc phải giống key trong dict

#IV. packing vs **:

def kteam(**kwargs):
	print(kwargs)
	print(type(kwargs))
kteam(name="nhat",last="huhhu") #Nó biến các tham số sẽ có dạng dict