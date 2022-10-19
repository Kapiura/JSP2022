a=int(input())
b=int(input())
if b>a:
	print("b>a")
	quit
else:
	Z=b%a
	Z*=Z+3
	print(Z)
