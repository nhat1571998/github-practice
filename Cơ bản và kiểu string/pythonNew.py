# Lỗi vì type không thể đọc cùng với 1 chuỗi
# print("Hello "+type(name));
# Vào Tools + Build With... chọn Python
# Để chạy thì ấn ctrl+B


# I.Các kiểu dữ liệu số
# Các kiểu cơ bản k đề cập đến
#. Kiểu phân số:
from fractions import*
result = Fraction(6,9)
print(result);
# các giá trị sẽ được ép kiểu giống kiểu giá trị của vế phải

# Kiểu số thực:
result2 = complex(2,3)
print(result2.real)
print(result2.imag)
# Các phép tính lạ bên python: //: lấy phần nguyên vd: 10//3 = 3; ** lũy thừa vd: 2**3 = 8
#Thư viện: math trong python: import <tên thư viện>  dùng: <tên thư viện>.<tên hàm>

####          ----------Bài 8---------------
# Kiểu chuỗi:
# Chuỗi trần: tránh các trường hợp escape sequence
print('haiz, \neu em');
print(r'haiz, \neu em');
# các chuỗi bthuong các phép tính như các phép toán bthuong vd như * chuỗi
# Một số phép tính vs chuỗi: 
#1. in: ktra chuỗi A có nằm trong B k, kq: true, false. vd: strA in strB
#2. strA[3]: lấy ptu thuộc vị trí thứ 4 của strA, -1 thì nó đọc kí tự cuối cùng, -2 là gần cuối. Số lớn hơn chiều
#dài thì nó báo lỗi out of range. hàm len(strA): chiều dài chuỗi strA.
#3. cắt chuỗi: strA[1:4] lấy từ kí tự 2 đến 5 của chuỗi. None là auto vị trí cuối.
#4. Cắt chuỗi ngược: strA[1:4:x], trong đó x là bước nhảy: số dương là từ trái qua, số âm thì từ phải qua.
#5 thay đổi giá trị trong chuỗi: cắt cái chuỗi ra:
strA = "Hello123"
strA = strA[None:4]+"0"+strA[5: None]
print(strA);

####          ----------Bài 9---------------
# I. Phép gán % trong str:
#vd:
strC = "12"
strD = "%s %s"
strD1 = strD %("12","34");
strD2 = strD %("56","78");
strB = "Chào bạn %s %s Nhất" %(strC,"34")
print(strD1 +" "+ strD2)
print(strB)
# ta đã gán gtri %s bằng 12, như vd thì nó chỉ hiểu 1 hàng. 
# => Mục đích là có thể sử dụng lại 1 chuỗi mà không cần viết lại mà có thể gán rồi sài lại

# II. Gán chuỗi cho chuỗi:
#vd:
strVD92 = "Hello"
strVD921 = f"{strVD92} chào mn"
print(strVD921);
# f giúp python hiểu phải tìm thằng strVD92 để lấy gtri chuỗi chứ k phải in ra i hệt

# III. Format:
# gán gtri cho các phần tử:
#vd: 
strVD931 = 'a:{},b:{},c:{}'.format(1,2,3);
strVD932 = 'a:{2},b:{1},c:{0}'.format(1,2,3);
print(strVD931);
print(strVD932);
# thay đổi vị trí nhận giá trị được

####          ----------Bài 10---------------

#I. Viết hoa kí tự trong chuỗi.
#1. capitalize()
strVD1011 = "helLo"
strVD1012 = strVD1011.capitalize() # Đầu viết hoa tất cả các kí tự khác đều viết thường
print(strVD1012) 
#2. upper(), lower
strVD1013 = strVD1011.upper()
strVD1014 = strVD1011.upper()
#3. swapcase() đảo ngược hoa <-> thường.
#4. title() chuyển các kí tự đầu sau dấu " " thành viết hoa.
#5. a.join('1','2') cộng chuỗi a vào 1 rồi cộng tiếp chuỗi 2: "1"a"2"
#6. a.replace("a","b",x) thay tất cả kí tự "a" trong chuỗi a thành kí tự "b". Nếu có  x thì sẽ thêm đủ số lần x còn nếu k thì thêm cả.

####          ----------Bài 11---------------

#1. split("m",x): cắt ra các kí tự trong yêu cầu tạo ra 1 list: vd "Hello A" => split(" ") = ["Hello","A"], nếu có tham số x là số lần cắt
#2. count("x",a,b): đếm số chuỗi con x trong chuỗi cha từ vị trí a đến b.
#3. find("x"): tìm vị trí của phần tử x đầu tiên, nếu k có sẽ báo -1.
#4. islower, isupper: xác định chuỗi có phải viết thường, viết hoa k.
#5. isdigit: xác định giá trị trong chuỗi có phải là số hay k.
