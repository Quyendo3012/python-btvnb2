# Hàm tìm số lớn nhất
def findmax(a, b, c):
    max = a
    if max < b: max = b
    if max < c: max = c
    return max
 
a = float(input("Nhập vào số thứ nhất: "))
b = float(input("Nhập vào số thứ hai: "))
c = float(input("Nhập vào số thứ ba: ")) 

print("Số lớn nhất trong ba số ", a, " ", b, " ", c, " là ", findmax(a, b, c))