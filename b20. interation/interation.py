
#Interation hiểu chung là việc lấy từng ptu của một đối tượng nào đó, bất cứ khi nào có sử dụng vòng lặp hay kĩ thuật khác.

#I. Một số hàm đi vs interation
#1. Sum
a = sum([1,2,3],6) #Theo cách hiểu thì nó sẽ tính tổng giá trị trong list [1,2,3] rồi công vs ptu 10, tuy nhiên k thể cộng 2 list vs nhau.
print(a)

#2. max
b = [1,2,4,3]
d = [5,6]
c = (1,2,3,4) # b và c đều như nhau vs hàm max
maxb = max(b,default = "Không có giá trị")
maxmul = max(b,d) # so sánh 2 chuỗi thì k có default
print(maxb)

#3. min: tương tự max.

#4.sorted
#  sorted(iterable, /, *, key=None, reverse=False) True thì sẽ là từ lớn -> bé
print(sorted(b,reverse = True))