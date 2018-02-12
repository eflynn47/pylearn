def is_all_strings(it):
    return all(type(x) == str  for x in it) 

names = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
max_names = max(names, key=lambda n: len(n))

def extremes(it):
    return (min(it), max(it))

# def max_magnitude(li1):
#     return max(li1, key=lambda i: abs(i))

def max_magnitude(li1):
    return max(abs(i) for i in li1)



if __name__ == '__main__':
    print(is_all_strings(['a', 'b', 'c']))  #True
    print(is_all_strings([2,'a', 'b', 'c']))  #False
    print(is_all_strings(('hello', 'goodbye')))  #True
    
    print(max_names)

    print(extremes([1,2,3,4,5]))  # (1, 5)
    print(extremes((99,25,30,-7)))  # (-7, 99)
    print(extremes("alcatraz"))  #( 'a', 'z')

    print(sum([2,4,6,5,2,8,5,3,5,8]))
    print(sum([2,4,6,5,2,8,5,3,5,8], 100))
    print(max_magnitude([300, 20, -900]))   #900
    print(max_magnitude([10, 11, 12]))   #12
    print(max_magnitude([-5, -1, -89]))   #89
