#Lưu ý trong items của dict:
#Có thể ép kiểu về các kiểu dễ sử lý hơn: do thằng này k phải là iterator object, cũng k phải là interator có thể indexing
#vd:

dict1 = {'a':'14','b':'abc','c':'huhu'}
a = list(dict1.items())
print(a[0])
for key,val in dict1.items():
	print("key:",key," val:",val)

#Tương tự như là while-else, ta cũng có for- else: có nghĩa khi kết thúc for chạy else.



#---------------------------- bài tiếp theo ------------------------

#I. range()
#range(start, stop[, step])

# print(list(range(2,5)))
# print(list(range(2,-8,-2))) # đọc đến end -1
#range() thì có tốc độ sử lý nhanh hơn so vs 1 list tương tự như range()

lst = ["s", (1, 2, 3), {'abc', 'xyz'}]
for i in range(len(lst)):
	print(lst[i])

# Sự khác nhau giữa sequence scan và indexing scan.
print("\nVd sự khác nhau giữa sequence scan và indexing scan")
lst = [1,2,3,4]
for value in lst:
	value += 1
print("dung sequence scan",lst)

for x in range(len(lst)):
	lst[x] += 1
print("dung indexing scan",lst)

#II. comprehension
#[ output-expression for-statement optional-predicate ]
print("\nComprehension")
lst = ['--'.join((a.capitalize(), b.upper() + c.lower())) for a, b, c in [('how', 'kteam', 'EDUCATION'), ('chia', 'sẻ', 'FREE')]] 
# bỏ trống optional-pre
print(lst)
#Trong này ta có thể hiểu: nguyên văn đoạn đầu trong ngoặc đến for là câu lệnh, a,b,c là tham số, sau in là giá trị

#vd2: >>> {key:value + 1 for key, value in (('Kteam', 69), ('Tèo', 50), ('Tũn', 14), ('Free Education', 93)) if value % 2 != 0}
# viết bthuong
dictx = {}
for key,val in (('Kteam', 69), ('Tèo', 50), ('Tũn', 14), ('Free Education', 93)):
	if(val%2 != 0):
		val += 1
		dictx[key] = val
print(dictx)

#III. Hàm enumerate.
#enumerate(iterable[, start])

student_list = ['Long', 'Trung', 'Giàu', 'Thành'] # list,tuple,dict đều oke
gen = enumerate(student_list,1) # trong đó student_list là tham số truyền vào, 1 là điểm bắt đầu:
lstIII = list(gen)
for key,val in lstIII:
	print('key:',key,"-- val:",val)