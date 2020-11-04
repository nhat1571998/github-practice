

# Giới thiệu tổng quan: Dict (Dictionary) là container như list, tuple. tuy nhiên thay vì dùng index để tìm kiếm cũng như truy xuất dữ liệu
# dict sử dụng key.
# Cấu trúc cơ bản tương tự như thằng Set: tuy nhiên thì trong 1 ptu phải có 2 giá trị: key, value, ngăn cách bởi dấu :. key bắt bắt buộc phải
# là hashable object

#Dict Comprehension
dic = {key: value for key, value in [('name', 'Kteam'), ('member', 69)]}
print(dic)

#Sự lợi hại của dict: Khi mà nta truyền vào 1 cái gì đó là mk có thể lấy ra ngay giá trị mà mk cần.

#Vì dict là 1 unhashable nên ta có thể thay đổi giá trị 1 cách đơn giản: như list

#I. Các phương thức của kiểu Dict
#1. copy
dic2 ={"name":"Ann","age":"18"}
dic3 =dic2.copy()
dic3.clear()
print(dic2)
print(dic3)

#2.get: lấy value theo key, nếu k có key thì ra none
val = dic2.get('name','Không tồn tại') # nếu k có giá trị sẽ báo không tồn tại
val2 = dic2.get('aa','Không tồn tại')
print(val)
print(val2)

#3. items: lấy 1 tuple có key và value
print("Vd về items")
items = dic2.items()
print(items)
#Nếu muốn lấy từng item trong này thì cần chuyển nó thành list:
listItem = list(items)
print(listItem[0][1]) #Nếu gtri truyền vào key,val k tồn tại thì sẽ bị báo lỗi

#4. keys,values: Lấy ra danh sách keys, values trong dict:
print(dic2.values())
print(dic2.keys())

#5.pop: Lấy ra val của key truyển vào và xóa luôn ptu trong dict, nếu k có key sẽ báo lỗi, tuy nhiên nếu thêm defaul (như vd trên) thì
#sẽ không còn lỗi nữa mà báo ra giá trị mk cho phép:
valpop = dic2.pop('name')
print(valpop)
print(dic2)

#6.setdefault: Lấy ra giá trị trong dict, nếu như k tồn tại sẽ tạo 1 ptu mới trong dict
valsetd = dic2.setdefault('address')
valsetd2 = dic2.setdefault('age','19')
valsetd2 = dic2.setdefault('huhu','19') # nếu như thêm vào sau key 1 val thì nó sẽ thêm val đó làm value mới (nếu key có trong dict thì
# không bị ảnh hưởng)
print(valsetd2)
print(dic2)

#7. update
#vd1:
print("VD7: Update:")
dic7 = {'a':1}
dic7.update(B =2,C =3)
print(dic7)
E = [('D',4),('E',5)]
dic7.update(E)
print(dic7)
E2 = (['E',6],['G',7]) #Nếu key tồn tại sẽ update giá trị của thằng value
dic7.update(E2)
print(dic7)