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

def sum_even_values(*args):
    return sum(i for i in args if i%2 == 0)

def sum_floats(*args):
    return sum( i for i in args if type(i)==float)

# def interleave(st1, st2):
#     li1 = zip(st1, st2)
#     newstr = ''
#     for t in li1:
#         for c in t:
#             newstr += c
#     return newstr

def interleave(st1, st2):
    return ''.join(''.join(t) for t in (zip(st1, st2)))

def triple_and_filter(li1):
    return [i*3 for i in filter(lambda x: x%4==0  , li1)]

# def extract_full_name(li1):
#     newli = []
#     for dict1 in names:
#         newli.append(dict1['first'] + ' ' + dict1['last']) 
#     return newli

# def extract_full_name(li1):
#     return [ dict1['first'] + ' ' + dict1['last']  for dict1 in li1]

def extract_full_name(li1):
    return list(map(lambda x: "{} {}".format(x['first'], x['last'])  , li1))


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

    print(sum_even_values(1,2,3,4,5,6)) # 12
    print(sum_even_values(4,2,1,10)) # 16
    print(sum_even_values(1)) # 0

    print(sum_floats(1.5, 2.4, 'awesome', [], 1)) # 3.9
    print(sum_floats(1,2,3,4,5)) # 0

    print(interleave('hi','ha'))    # 'hhia'
    print(interleave('aaa', 'zzz'))  # 'azazaz'
    print(interleave('lzr','iad')) #  'lizard'

    print(triple_and_filter([1,2,3,4])) # [12]
    print(triple_and_filter([6,8,10,12])) # [24,36]

    names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
    print(extract_full_name(names)) # ['Elie Schoppik', 'Colt Steele']

    print("This is a test")