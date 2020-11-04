
#Lệnh return trả về 1 object tùy thuộc lựa chọn.

def cal_rec_per(width, height):
    per = (width + height) * 2
    return per

rec_1_width = 5
rec_1_height = 3
# khởi tạo một biến để hứng kết quả
rec_1_per = cal_rec_per(rec_1_width, rec_1_height)
print(rec_1_per)
# trường hợp này là khi bạn không cần tái sử dụng nó ở lần sau
print(cal_rec_per(7, 4))


#Dùng return trả nhiều gia trị 1 lúc:

def cal_rec_area_per(width, height):
    perimeter = (width + height) * 2
    area = width * height
    return perimeter, area
rec_width = 3
rec_height = 9
rec_per, rec_area = cal_rec_area_per(rec_width, rec_height)

print("vd 2:",rec_per, rec_area)