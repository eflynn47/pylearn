
def contains_keyword(*args):
    for arg in args:
        if keyword.iskeyword(arg):
            return True
    return False    
    
    
    


if __name__ == '__main__':
    import keyword

    print(contains_keyword("hello", "goodbye"))  #False
    print(contains_keyword("def", "haha", "lol", "chicken", "alaska"))  #True
    print(contains_keyword("four", "for", "if"))  #True
    print(contains_keyword("blah", "doggo", "crab", "anchor"))  #False)
    print(contains_keyword("grizzly", "ignore", "return", "False"))  #True
