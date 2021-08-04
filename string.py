str1="int"
print("str1:",id(str1))
str2="char"
print("str2:",id(str2))
str1=str1+str2
print("str1:",id(str1))
x=12
print("int value:%d"%x)
s="string"
c=0
for i in s:
	print("s[%d]:"%c,i)
c+=1
s=s.capitalize()
print(s)
s=s.center(10,'*')
print(s)
s="is string"
substring="is"
count=s.count(substring)
print("count is:",count)
print(s.isalnum())
s="aaAA"
print(s.isalpha())
print(s.isupper())
print(s.upper())
print(s.swapcase())
str="     python lang"
print(str.lstrip())
print(str.rstrip())
print(str.split())





