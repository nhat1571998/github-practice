#Tương tự các ngôn ngữ khác:

# a = [1,2,3,4]
# b = "Hello Mn"
# m = len(b)
# print("Chiều dài:",m)
# x = 0
# while m>x:
# 	print("Giá trị là",b[0+x])
# 	x += 1
# 	if x ==3:
# 		print("Thoát")
# 		break #Chú ý nếu có 2 vòng lặp lồng thì break chỉ thoát vòng con
# 	if x ==2:
# 		print("Tiếp")
# 		continue
# 	print("Huhu") #continue sẽ bỏ qua câu lệnh này mà chạy luôn lên trên
# else:
# 	print("Kết thúc vòng lặp") # Như đã thấy break nó khiến kết thúc cả vòng lặp lẫn câu lệnh else trên.


# #Vòng while else:
# k = 3
# while k>0:
# 	print(k)
# 	k -= 1
# else:
# 	print("Kết thúc vòng lặp")


#Câu hỏi cũng cố
# Bài 1:
file_object = open('bt.txt', mode="a+")
file_object.seek(0)
data = file_object.read()
print("data:\n",data,sep="")
x = data.split(' ')
length = len(x)
print(length)
count = 0
file_object.close()
file_object = open('bt.txt', mode="w+")
while count<length:
	if x[count] == "Kteam":
		x[count] = "How"
	write = file_object.write(x[count])
	write2 = file_object.write(" ")
	count +=1
else:
	file_object.close()

# bài 2:
b2 = [56, 14, 11, 756, 34, 90, 11, 11, 65, 0, 11, 35]
