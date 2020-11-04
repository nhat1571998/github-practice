#Container: Cho phép ta lưu trữ, giữ các giá trị cho một cụm
# List có 2 cách khởi tạo:
#C1: a = [1,2,3,4] và a = List("abcd") và bắt buộc "abcd" phải là kiểu tập hợp (nhiều pt)
#I. Các toán tử trong list
a = [1,2]
b = [7,6,9,3,4]
#1. Cộng
c = a +b
print(c)
#2. Nhân 1 chuỗi nhiều lần
d = a*2
print(d)
#3. in: ktra 1 phần tử có thuộc list
e = "1"
f = e in a
print(f)
#4. đảo ngược list
g = [1,2,3,[4,5]]
h = g[::-1] # bằng với g.reverse()
print(g[2:])
print(h)
#5. Thay đổi giá trị phần tử trong list. Chỉ cần gọi và thay đổi
a[1] = "2"
print(a)
# Warning: Không được gán list a = list b vì đây là kiểu tham chiếu => nó sẽ thay đổi cả dữ liệu ban đầu
#Cách sửa: b = List(a) => Nó sẽ tạo 1 list mới cho b có giá trị tương tự list a
# sử dụng hàm copy b = a.copy()

#clear: Xóa bỏ các phần tử trong list

#II. Các phương thức trong list

#1. append: thêm phần tử vào list
#2. extend: như append tuy nhiên khi thêm 1 list thì thay vì gán cả list mới đó là 1 ptu thì nó sẽ tự lấy từng ptu trong đó để thành ptu con
#(nhưng chỉ 1 bậc)
#3. insert: a.insert(1,2) thêm ptu 2 vào vị trí 1 trong list a, nếu số vị trí >= len của list thì tự thêm vào cuối, số âm thì đếm ngược
#4. pop: a.pop(x) lấy ptu tại vị trí x của a( a mất luôn ptu đó)
#5. remove: a.remove(x): xóa ptu x đầu tiên trong list a, nếu k có sẽ bị lỗi
#6. sort(): a.sort(): mặc định sắp xếp từ bé đến lớn, và ptu trong sort phải cùng kiểu dữ liệu.
#Trong sort có 2 tham số: sort(key=None,reverse=False) => True nó sẽ đảo ngược
b.sort()
print(b)

#vd:

lista = [1,2,3,4]
listb = lista
listb += [4,5]
print("VD bt")
print(listb)
print(lista)