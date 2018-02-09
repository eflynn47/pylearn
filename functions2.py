
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