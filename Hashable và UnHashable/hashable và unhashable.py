#list là 1 unhashable object
#str, tuple là 1 hashable object
#Khi sử dụng toán tử += thì thằng unhashable k thay đổi địa chỉ lưu trữ vì nó vẫn được nằm tại vị trí cũ.
#Trong khi đó thằng hash bộ nhớ sẽ k để sẵn vị trí trống sau nó mà phải tìm một nơi mới để đặt giá trị mới vào.

a = [1,2,3];
b = id(a)
print(b)
a = a + [4];
print(a);
print(id(a))
a += [4]
print(id(a))