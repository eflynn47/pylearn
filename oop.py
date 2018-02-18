class User:
    def __init__(self, first, last='Doe', age=0):
        self.first = first
        self.last = last
        self.age = age

class Comment:
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes

class Person:
    def __init__(self, name):
        self.name = name
        self._secret = "My Balls are Blue!" #//_secret is only convention - no such thing as secret attributes in Python
        self.__msg = "I Like Turtles!"  #name mangling - used to help make this attribute particular to this class
    def doorman(self, guess):
        if guess == self._secret:
            return "Come In!"
        else:
            return "Stay Out MuthaFukka!!!"    

if __name__ == '__main__':
    
    user1 = User("Joe", "Animal", 44)
    user2 = User("Georgie", "Puddintang", 23)
    user3 = User("Asshole", "McPants", 14)
    print(user1.first, user1.last, user1.age)
    print(user2.first, user2.last, user2.age)
    print(user3.first, user3.last, user3.age)

    c = Comment("davey123", "lol you're so silly", 3) 
    print(c. username)       #"davey123"
    print(c. text)           #"lol you're so silly"
    print(c.likes)           #3

    another_comment = Comment("rosa77", "soooo cute!!!") 
    print(another_comment.username)        #"rosa77"
    print(another_comment.text)            #"soooo cute!!!"
    print(another_comment.likes)           #0 

    p = Person("Harry")
    print(p.name)
    print("\n")
    print(p.doorman("Blue Balls"))
    print(p.doorman("My Balls are Blue!"))
    print(p._Person__msg)  #must access msg this way
