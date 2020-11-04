# Tuple nằm giữa dấu (), các ptu ngan bởi dấu ",",chứa được mọi gtri và ngăn giá trị bị thay đối.
# Tốc độ truy xuất nhanh hơn list, du lượng nhỏ hơn list, có thể dùng làm key của dictionaty.

#Sự khác biệt giữa tuple vs list:
#Tuple giống như str là không thể thay đổi giá trị ptu trong tuple


tup = (2,3,4)
print(tup)
tup2 = tup
tup2 += (5,6)
print(tup2)
print(tup)
