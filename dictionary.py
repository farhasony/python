dict={"1":"c","2":"cpp"}
dict["3"]="python"
print(dict)
d={"4":"java"}
x=d.copy()
print(x)
x=dict.fromkeys(d)
print(x)
x=d.get("4")
print(x)
x=d.items()
print(x)
x=d.keys()
print(x)
d.values()
print(x)
d.update(dict)
print(d)

