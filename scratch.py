
nums = [1,2,3]
name = 'butthead'
nums2 = [1,2,3,4,5,6]

listcomp = [x*10 for x in nums]
listcompname = [c.upper() for c in name]
listtype = [str(n) for n in nums]
evens = [n2 for n2 in nums2 if n2 % 2 == 0]

print(listcomp)
print(listcompname)
print(listtype)
print(evens)

answer = [c[0] for c in ["Elie", "Tim", "Matt"]]
print(answer)

answer2 = [n for n in [1,2,3,4] if n in [3,4,5,6]]
print (answer2)

answer3 = [n[::-1].lower() for n in ["Elie", "Tim", "Matt"]]
print(answer3)

answer4 = [n for n in range(1, 101) if n% 12 == 0]
print(answer4)

answer5 = [c for c in 'amazing' if c not in 'aeiou']
print(answer5)