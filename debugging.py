def eric_func(a, b):
    try:
        li = [a + i for i in b]
    except:
        return "You suck"
    else:
        print("I'm in the else!")
        return li
    finally:
        print("I'm in the finally!")
       
def divide(num1, num2):
    try:
        div1 = num1//num2
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
    else:
        return div1



if __name__ == '__main__':
    #import pdb; pdb.set_trace()

    li1 = list(range(1, 41))
    print(li1)
    print(eric_func(10, 'ass'))
    print("After the Try:")

    print(divide(4,2)) # 2
    print(divide([],"1")) # "Please provide two integers or floats"
    print(divide(1,0)) # "Please do not divide by zero"
    