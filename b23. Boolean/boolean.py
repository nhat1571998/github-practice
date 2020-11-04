#Chú ý về các toán tử so sánh: nếu dùng ==, >=,<= thì Python sẽ so hết các ptu, còn nếu chỉ sử dụng >,<,!= thì chỉ cần 1 ptu khác thì 
#Python sẽ trả ngay kq = False

#Toán tử: is
#Khác vs == là ở chỗ is không so sánh giá trị mà còn so sánh có thuộc cùng 1 đối tượng hay không nữa.
lst = [1,2,3]
lst2 = lst
lst3 = [1,2,3]
print(lst == lst3)
print(lst is lst3)
print(lst == lst2)
print(lst is lst2) # true là bới vì 2 thằng lst và lst2 cùng trỏ đến cùng một vùng nhớ
#Vấn đề: giá trị từ -5 đến 256 hoặc các chuỗi có số kí tự < 20 thì is sẽ trả về true.

#Toán tử: NOT,AND,OR

#Tất cả các giá trị chuyển về boolean đều là true ngoại trừ các th: 0, none, rỗng.

#So sánh giá trị thuộc khoảng và giá trị bằng:
print("vd về việc so sánh khoảng và thuộc 1 interation")
a = 5
m = 4<a<7
print(m)
n = a in (range(1,2))
print(n)