
nums = [1,2,3]
name = 'butthead'

listcomp = [x*10 for x in nums]
listcompname = [c.upper() for c in name]
listtype = [str(n) for n in nums]

print(listcomp)
print(listcompname)
print(listtype)