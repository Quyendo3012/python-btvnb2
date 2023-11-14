def total(n):
    total = 0
    while (n > 0):
        total = total + n % 10 #Lấy dư rồi cộng dư vào total
        n = int(n / 10) #Xóa chữ số cuối = phép chia lấy phần nguyên đến bao h bằng 0 thì thôi 

    return total
 
n = int(input("Nhập n = "))
print("Tổng các chữ số của", n , "là", total(n))

# % là chia lấy phần dư 
# / chia các giá trị cho nhau lấy nguyên