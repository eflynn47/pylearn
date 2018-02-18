
def contains_keyword(*args):
    for arg in args:
        if keyword.iskeyword(arg):
            return True
    return False


def print_msg(user_text, user_color):
    available_colors = (
        'red',
        'green',
        'yellow',
        'blue',
        'magenta',
        'cyan',
        'white')
    if user_color not in available_colors:
        user_color = 'green'
    new_text = figlet_format(user_text)
    color_text = colored(new_text, color=user_color)
    print(color_text)


if __name__ == '__main__':
    import keyword
    from termcolor import colored
    from pyfiglet import figlet_format

    print(contains_keyword("hello", "goodbye"))  # False
    print(contains_keyword("def", "haha", "lol", "chicken", "alaska"))  # True
    print(contains_keyword("four", "for", "if"))  # True
    print(contains_keyword("blah", "doggo", "crab", "anchor"))  # False)
    print(contains_keyword("grizzly", "ignore", "return", "False"))  # True

    user_text = input("What chu want to print bitch? ")
    user_color = input("What Color do you want? ")
    print_msg(user_text, user_color)
