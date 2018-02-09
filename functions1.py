from random import random

def say_hi():
    print("Hi!")

def sing():
    print("Rock and Roll ain't noise polution")

def print_square(num):
    return num**2

def flip_coin():
    #generate random number 0-1
    if random() > 0.5:
        return "Heads"
    else:
        return "Tails"

def generate_evens():
    return [ i for i in range(1, 50) if i % 2 == 0]

def yell(string1):
    return "{}!".format(string1.upper())

def speak(animal='dog'):
    """Will print the noise the animal makes"""
    if animal == 'pig':
        return 'oink'
    elif animal == 'duck':
        return 'quack'
    elif animal == 'cat':
        return 'meow'
    elif animal == 'dog':
        return 'woof'
    else:
        return '?'


days_of_week = {
    1: 'Sunday',
    2: 'Monday',
    3: 'Tuesday',
    4: 'Wednesday',
    5: 'Thursday',
    6: 'Friday',
    7: 'Saturday',
}

def return_day(num):
    return days_of_week.get(num)    

last_el = []

def last_element(list1):
    if list1:
        return list1[-1]
    return None

def number_compare(a, b):
    if a > b:
        return "First is greater"
    elif a < b:
        return "Second is greater"
    else:
        return "Numbers are equal"

'''
single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
'''

def single_letter_count(s, c):
    s1 = s.upper()
    s2 = s.lower()
    if c.isupper():
        return s1.count(c)
    return s2.count(c)

def single_letter_count2(s, c):
    return s.lower().count(c.lower())

if __name__ == "__main__":
    say_hi()
    sing()
    print(f"The Square of 4 is: {print_square(4)}") 
    print(flip_coin())
    print(generate_evens())
    print(yell("help me"))
    print(speak('pig'))
    print(speak.__doc__)
    print(return_day(87))
    print(last_element(last_el))
    print(number_compare(2,4))
    print(single_letter_count("Hello World", "h"))
    print(single_letter_count2("Hello World", "L"))