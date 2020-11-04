# Set là 1 container tương tự như là list và tuple, tuy nhiên không được sử dụng nhiều như 2 cái này.
# Quan trọng: Set không chứa các phần tử trùng lặp vd: 1,1,2,3,2 => 1,2,3
a = {1,1,2,3,2}
print(a)

#I. Cấu trúc cơ bản của Set:
# chứa trong dấu {}, các ptu ngăn cách nhau bằng dấu ",", không thể chứa 1 set con (có thể chứa các hashable object nhưng k phải hash...),
# không thể chứa unhashable object trong bất kì vị trí nào (vd như là list), tạo empty set chỉ bằng contructor
# Set không quan tâm vị trí của các ptu 

#II. Các toán tử trong set:
# 1. Trừ set:
b = {1,2}
c = {3,2}
print(b-c)
# 2. & set:
print(b&c)
# 3. | set:
print(b|c)
# 4. ^ set:
print(b^c)

#III. Các phương thức cơ bản:
# 1. clear:
b.clear()
print(b)
# 2. pop: pop là lấy giá trị đó ra khỏi a luôn.
m = a.pop()
print(a)
print(m)
# 3.remove: nếu không có giá trị thì báo lỗi.
a.remove(2)
print(a)
# 4. discard: xóa đi 1 ptu nhưng nếu không tồn tại cũng sẽ k báo lỗi
# 5. copy: copy 1 set.
# 6. add: Khi thêm giá trị bằng add thì nó sẽ k thay đổi địa chỉ của set.
a.add(5)
print(a)

#Bài tập củng cố.
m ={1,2}
n = set(m)
n.clear()
print(m)