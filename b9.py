from this import d


d,m,y = int(input("Nhập ngày: "))
m = int(input("Nhập tháng: "))
y = int(input("Nhập năm: "))

if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0) and (d==29) and (m==2):    
    dnext = 1
    mnext = 3
    ynext = y
    print(dnext, mnext, ynext , sep="/")
else:
    if (m == 2) and (d <= 28) and (m<12):
        if d == 28:
            dnext = 1
            mnext = m+1
            ynext = y
            print(dnext, mnext, ynext,  sep="/")
        else:
            dnext = d+1
            mnext = m
            ynext = y
            print(dnext, mnext, ynext, sep="/")
    elif (m == 4) or (m == 6) or (m == 9) or (m == 11) and (d <= 30) and (m<12):
        if d == 30:
            dnext = 1
            mnext = m+1
            ynext = y
            print(dnext, mnext, ynext, sep="/")
        else:
            dnext = d+1
            mnext = m
            ynext = y
            print(dnext, mnext, ynext, sep="/")
    elif (m == 1) or (m == 3) or (m == 5 )or (m == 7) or (m == 8) or (m == 10) and (d <= 31) and (m<12):
        if d == 31:
            dnext = 1
            mnext = m+1
            ynext = y
            print(dnext, mnext, ynext, sep="/")
        else:
            dnext = d+1
            mnext = m
            ynext = y
            print(dnext, mnext, ynext, sep="/")
    elif (m == 12) and (d <= 31):
        if d == 31:
            dnext = 1
            mnext = 1
            ynext = y
            print(dnext, mnext, ynext, sep="/")
        else:
            dnext = d+1
            mnext = m
            ynext = y
            print(dnext, mnext, ynext, sep="/")
    else:
        print("Ngày tháng năm không hợp lệ")