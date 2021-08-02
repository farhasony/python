#a=int(input())
x=lambda a:a*10
print(x(100))
x=lambda a:a/10
print(x(100))
x=lambda a:a%10
print(x(100))
def fact(x):
	if x==1:
		return 1
	else:
		return(x*fact(x-1))
x=int(input())
print(fact(x))
	
