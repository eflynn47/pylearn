
def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total

def contains_purple(*args):
    return 'purple' in args

def combine_words(s1, **kwargs):
    if 'prefix' in kwargs and 'suffix' in kwargs:
        return f"{kwargs['prefix']}{s1}{kwargs['suffix']}"
    elif 'prefix' in kwargs:
        return f"{kwargs['prefix']}{s1}"
    elif 'suffix' in kwargs:
        return f"{s1}{kwargs['suffix']}"
    else:
        return {s1}

# NO TOUCHING! =================================================================
def count_sevens(*args):
    return args.count(7)

nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]
# NO TOUCHING! =================================================================

# Write your code below:

result1 = count_sevens(1,4,7)
result2 = count_sevens(*nums)
        
def calculate(**kwargs):
    if kwargs['operation'] == 'add':
        math = kwargs['first'] + kwargs['second']
    elif kwargs['operation'] == 'subtract':
        math = kwargs['first'] - kwargs['second']
    elif kwargs['operation'] == 'multiply':
        math = kwargs['first'] * kwargs['second']
    else:
        math = kwargs['first'] / kwargs['second']
    if kwargs['make_float']:
        math = float(math)
    else:
        math = int(math)
    if kwargs.get('message'):
        return "{} {}".format(kwargs['message'], math)
    else:
        return "The result is {}".format(math)

    



if __name__ == '__main__':
    print(sum_all_nums(1,4,2,8,45,20))

    print(contains_purple(25, "purple"))   #True
    print(contains_purple("green", False, 37, "blue", "hello world"))   #False
    print(contains_purple("purple"))   #True
    print(contains_purple("a", 99, "blah blah blah", 1, True, False, "purple"))   #True
    print(contains_purple(1,2,3))  #False

    print(combine_words("child"))  #'child'
    print(combine_words("child", prefix="man"))  #'manchild'
    print(combine_words("child", suffix="ish"))  #'childish'
    print(combine_words("work", suffix="er"))  #'worker'
    print(combine_words("work", prefix="home"))  #'homework'
    print(combine_words("work", prefix="home", suffix="er"))  #'homeworker'

    print(result1)
    print(result2)

    print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4)) # "You just added 6"
    print(calculate(make_float=True, operation='divide', first=3.5, second=5)) # "The result is 0.7"
