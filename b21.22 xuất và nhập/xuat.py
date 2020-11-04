
#print
#  print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
#Trong đó

#1. objects:
# chính là packing argument. Ở đây hiểu nôm na sẽ là nó sẽ gom lại các argument của bạn lại thành một Tuple.
print("Hello","My name is Nhat") # nó sẽ gộp 2 str thành 1 tuple rồi in ra, giữa 2 str sẽ tự có 1 dấu " "
a = [1,2,3,5,4]
print("Hello",a) #Không cần ép kiểu chỉ cần có dấu ","

#2. sep: Mặc định giá trị chèn giữa 2 objects
print("hello","my name is nhat", sep=" <> ")

#3. end: Mặc định giá trị kết thúc 1 câu lệnh print:
#print(a,end="|||")
from time import sleep #hàm sleep từ thư viện time.
print("Start...", end='') #Không hiểu nhưng nó lại xuất ra ngay cho dù end = "", theo như trong bài ns thì nếu có kí tự newline(" ") 
#thì nó mới in, hoặc chỉ khi kết thúc ctrinh thì nó mới in ra.
sleep(3)
print("End...")

#4. file: Ghi print vào file:
#vd file:
with open('vd_xuat.txt','w') as f:
	print("Xin chào!", file=f)

#5.flush: mặc định là false, nếu flush = True thì nó sẽ yêu cầu bộ đệm xuất tất cả giá trị ra.
from time import sleep #hàm sleep từ thư viện time.
print("Start...", end='',flush =False)
sleep(3)
print("End...")