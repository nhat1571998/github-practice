
#Thao tác vs file

#1. open()
file_object = open('vd.txt')
print(file_object)
#Một số mode: r,w,a: khác nhau ở chỗ w sẽ xóa dữ liệu trong file. w,a sẽ tạo file mới nếu k tồn tại file có tên tìm kiếm, + cho phép
# vừa ghi vừa đọc

#2. read()
#size: nếu size âm hoặc bỏ trống thì sẽ đọc hết file và con trỏ sẽ nằm ở vị trí cuối cùng. còn nếu k sẽ đọc số kí tự = size hoặc hết file
data = file_object.read()
print(data)
# vì con trỏ nằm ở cuối file nên k thể đọc được nữa. bắt buộc file đóng file ròi mở lại ms có thể đọc lại
file_object.close()
file_object = open('vd.txt')
data2 = file_object.read()
print(data2)
file_object.close()

#3.readline
file_object = open('vd.txt')
data3 =file_object.readline()
#vì file_object là các interable nên có thể sử lý như list, tuple:
data4 = list(file_object) # tuple(file_object)
print(data4)
file_object.close()

#4. write
file_object = open('vd.txt', mode ='a+')
write = file_object.write('\nLe Van Nhat')
dataw = file_object.read()
print(dataw)

#5.seek: đưa con trỏ về vị trí cụ thể.
file_object.seek(0) # trở về vị trí ban đầu
dataw = file_object.read()
print(dataw)