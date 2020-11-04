
#Ngoài việc định nghĩa hàm sử dụng từ khóa def ra thì nta còn 1 cách tạo khác đó là dùng lambda, tuy nhiên def tạo 1 hàm
# vs 1 cái tên thì thằng lambda trả về 1 hàm. Thế nên nta hay gọi nó là hàm nạc danh (anonymous).

#Cú pháp:
#	lambda argument_1, argument_2, …, argument_n : expression

#lambda là một expression, không phải là một câu lệnh.

k = lambda x,y=2: x+y+1
z = k(4)
z2 = k(1,2)
print(z)
print(z2)

#Vd về lambda trong def:

def vd2():
	x = lambda z: z+2
	return x # trả về 1 function nạc danh
m = vd2()
print("vd 2 về lambda trong def",m(5)) # ta hiểu 5 ở đây chính là truyền giá trị cho hàm lambda chứ k phải cho parameter của def


#II. Câu đk cho lambda:

vd3 = lambda x,y: x if x >y else y
print(vd3(1,2))

#Câu lệnh if lồng nhau trong lambda
cd_of_2_3 = lambda x: (1 if x % 3 == 0 else 0) if x % 2 == 0 else 0
print("if lồng nhau",cd_of_2_3(5)) 

#III. Chồng các lambda: #Chồng thì có thể nhưng k được khuyển khích tẹo nào

kteam = lambda first_string: (lambda second_string: first_string + second_string)
vd31 = kteam("đây là first_string ")
print(vd31("đây là second_string"))

