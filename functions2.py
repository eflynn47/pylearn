
def is_palindrome(s):
    s1 = s.lower().replace(" ", "")
    return s1 == s1[::-1]

def frequency(li, search):
    return li.count(search)

def multiply_even_numbers(li):
    total = 1
    for num in li:
        if num %2 == 0:
            total *= num
    return total

def capitalize(s):
    return s[0].upper() + s[1:]

# def compact(li):
#     new_li = []
#     for val in li:
#         if val:
#             new_li.append(val)
#     return new_li

def compact(li):
    return [val for val in li if val]

def intersection(li1, li2):
    return [ val for val in set(li1).intersection(set(li2))]

def isEven(num):
    return num % 2 == 0

# def partition(li1, func):
#     tlist = []
#     flist = []
#     for val in li1:
#         if func(val):
#             tlist.append(val)
#         else:
#             flist.append(val)
#     return [tlist, flist]

def partition(li1, func):
    return [[val for val in li1 if func(val)], [val for val in li1 if not func(val)]]


if __name__ == "__main__":
    print(is_palindrome('testing')) # False
    print(is_palindrome('tacocat')) # True
    print(is_palindrome('hannah')) # True
    print(is_palindrome('robert')) # False
    print(is_palindrome('amanaplanacanalpanama')) # True
    print(is_palindrome('a man a plan a canal Panama')) # True

    print(frequency([1,2,3,4,4,4], 4)) # 3
    print(frequency([True, False, True, True], False)) # 1

    print(multiply_even_numbers([2,3,4,5,6])) #48

    print(capitalize("tim")) # "Tim"
    print(capitalize("matt")) # "Matt"

    print(compact([0,1,2,"",[], False, {}, None, "All done"])) # [1,2, "All done"]

    print(intersection([1,2,3], [2,3,4]))    #[2,3]
    print(intersection(['a','b','z'], ['x','y','z']))  # ['z']

    print(partition([1,2,3,4], isEven)) # [[2,4],[1,3]]