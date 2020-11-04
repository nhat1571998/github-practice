
# #I. Khởi tạo hàm:
# def <function_name>(parameter_1, parameter_2, .., parameter_n):

#     function-block

#Lưu ý: Lệnh pass được hiểu là 1 placeholder statment để giữ chỗ, tránh để trong block function bị thiếu.

#II. parameter và argument:

def newfunc(text):
	print("Hello",text);

newfunc("huhu")

# => Trong này thì text là parameter và huhu là argument.

# default argument: mặc định là argument này, nếu có thay đổi sẽ nhận thay đổi:
#Chú ý: default argument luôn phải nằm sau cùng, cũng là 1 unhasable container:
def name(a,b="Nhất"):
	print(a,b)

name("Hello")
name("Hi","Hung")

#Chú ý nè:
def f(kteam=[]):
	kteam.append('K')
	print(kteam)

for i in range(3):
	f() #Chúng ta có thể thấy, biến kteam đã được thêm "K" sau mỗi lần gọi. và kteam nó sẽ luôn giữ giá trị đó cho dù truyền 1 argument mới.
