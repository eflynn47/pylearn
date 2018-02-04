
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

#create list like [[1,2,3],[1,2,3],[1,2,3]] with comprehension
board = [[x for x in range(1,4)]  for n in range(1,4)]
print(board)

#create list like [['X','O','X'],['X','O','X'],['X','O','X']] with comprehension
kiss = [['X' if nu % 2 != 0 else 'O' for nu in range(1,6)] for val in range(1,4)] 
print(kiss)

#use nested list comp to create [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
answer6 = [[x for x in range(3)] for n in range(3)]
print(answer6)

answer7 = [[x for x in range(10)] for n in range(10)]
print(answer7)