elements ={"hi": 1,"whats": 2,"up": 3}
elements["what"]=33
print(elements)
print(elements["hi"]," ",elements["what"])
x=elements.get("NO")
isNull = x is None
isNotNull = x is not None
print(isNull)
print(isNotNull)