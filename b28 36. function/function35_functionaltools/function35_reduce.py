
#from functools import reduce

#Cú pháp: reduce(function, sequence[, initial])


#Hàm này có thể hiểu là: nó sẽ lấy 2 giá trị đầu index 0, index 1 cho vào function, kq trả về là A rồi đưa cái index 2 cùng vs A thành
# 1 cặp A index 2 gán vào function => cứ như vậy đên hết.
from functools import reduce

#vd hàm tính tổng chuỗi.

lst = [1,2,3,4,5]

kq = reduce(lambda x,y: x+y, lst) #Hàm reduce trả về 1 giá trị
print(kq)

#Còn nếu có initial sẽ gộp cái này vs index 0 trước

kq2 = reduce(lambda x,y: x+y,lst,6)
print("vd có initial",kq2)