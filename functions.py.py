def func():
	print("method1")
func()
def func(a,b):
	print("a:",a)
	print("b:",b)
	return a/b
print(func(100,10))
#default arg
def defaultArgs(a,b=10):
	print("a=",a,"b=",b)
	return
defaultArgs(10.00,40.0)
defaultArgs("hello","hi")
#keyword arg
def keywordArgs(a,b):
	print("a=",a,"b=",b)
keywordArgs(a=4,b="str")
#variable arg
def variableArgs(*a):
	print("array:",a)
	return
variableArgs(100,"str")
variableArgs(100.00,"str",10,)
	
