for_searching="python language"
s="python"
import re
pattern=re.compile(r'py')
result=re.match(pattern,s)
print(result)
result=re.search(r'language',for_searching)
print(result)
result=re.fullmatch(r'Python',s,flags=re.IGNORECASE)
print(result)
result=re.findall(r'python',s)
print(result)
result=re.sub(pattern,'py',for_searching)
print("sub:,",result)
string="12345 678, 9101 1111"
pattern='(\d{3}) (\d{2})'
match=re.search(pattern,string)
if match:
	print(match.group())
	print(match.start())
	print(match.end())
	print(match.span())
else:
	print("not found")
a="python python c cpp"
pattern=re.compile(r'c')
r=re.split(pattern,a)
print("split",r)
print(re.escape("1235.&&***"))

