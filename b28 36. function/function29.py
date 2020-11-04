# Truyền trực tiếp vào 1 cách bthuong thì gọi là positional argument, còn có cả parameter thì gọi là keyword argument..
# 2 thằng này có thể truyền cùng 1 lúc tuy nhiên thằng positional phải đứng trước password


#Có một số hàm bắt buộc chúng ta phải có password argument, vd: sort()
#Lợi ích: Cho những hàm có nhiều default argument:

def a(x,y=2,z=3):
	print(x+y+z)

a(1)

a(1,z=7) #Không cần truyền lại y.

# def function (*, key_arg1, key_arg2):

# # function-block

#Python sẽ tạo ra 1 hàm mà sau * sẽ bắt buộc phải truyền theo kiểu password argument nếu không sẽ bị lỗi.