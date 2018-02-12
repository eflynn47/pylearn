
add = lambda  a,b: a+b

cube = lambda num: num**3

nums = [2,4,6,8,10]
doubles = map(lambda n: n*2 , nums)

names = [
    {'first':'Rusty', 'last': 'Steele'},
    {'first':'Colt', 'last': 'Steele'},
    {'first':'Blue', 'last': 'Steele'},
]

first_names = list(map(lambda x: x['first']  , names))

def decrement_list(li1):
    return list(map(lambda x: x-1, li1))

def remove_negatives(li1):
    return list(filter(lambda x: x >= 0 , li1))


if __name__ == "__main__":
    print(add(3,8))
    print(add.__name__)

    print(cube(8))  # 512

    print(list(doubles))
    print(first_names)

    print(decrement_list([20,14,11]))
    print(remove_negatives([-1,3,4,-99]))
