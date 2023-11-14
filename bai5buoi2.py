def isfibo(a,b,n):
	t = a + b
	if t < n:
		return isfibo(b,t,n)
	elif t == n:
		return True
	else :
		return False

n = int(input("N = "))
if isfibo(0,1,n) or n == 0: print("True")
else : print("False")
