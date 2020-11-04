
#vd:
lst = [1,2,3,4]
def cal_sum(lst):
	return 0 if not lst else lst[0] + cal_sum(lst[1:]) # cấu trúc như rẽ nhánh trong lambda vậy ó
kq = cal_sum(lst)
print("vd1",kq)


#Sử dụng packing argument để cộng cả list, chuỗi. Tuy nhiên k thể sài vs container rỗng

def cal_sum2(lst):
	idx0, *r = lst # idx0, r = lst[0], lst[1:] #packing này như là kiểu làm 1 interable vào 1 biến vậy 
	return idx0 if not r else idx0 + cal_sum2(r)
print('dùng packing argument ở chỗ *r:',cal_sum2(lst))