def GiaiThua(n):
    gt = 1
    for i in range(1,n+1): gt = gt*i #gt: i!
    return gt
n = int(input("Nhập n = "))
s = 0
for i in range(1,n+1):
    s = s + GiaiThua(i) #s = s + i!
print("F(n) = ",s)

    
    