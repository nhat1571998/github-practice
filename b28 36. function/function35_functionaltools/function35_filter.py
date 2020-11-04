
#Hàm filter:
# filter(function or None, iterable)

#Tương tự như hàm map tuy nhiên thì nó sẽ ktra giá trị trong func nếu mà kq chuyển về boolean có nghĩa là true thì sẽ yield giá trị đó
# còn k thì bỏ qua.

lst = [1,-2,4,-3]

lst2 = list(filter(lambda x: x>0,lst))

print("vd1",lst2)

#Những giá trị như None, False sẽ bị loại bỏ qua hàm này.