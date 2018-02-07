# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW

if food in bakery_stock:
    print("{} left".format(bakery_stock[food]))
else:
    print("We don't make that")    


#DO NOT TOUCH game_properties!
game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notications", "achievements"] 

# Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0.  Save the result to a variabled called initial_game_state

initial_game_state = {}.fromkeys(game_properties, 0)
print(initial_game_state)

tea = bakery_stock.pop('tea cake')
print(tea)
print(bakery_stock)

inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
stock_list = inventory.copy()
print(stock_list)
# add the value 18 to stock_list under the key "cookie"
stock_list['cookie'] = 18
print(stock_list)
# remove 'cake' from stock_list USE A DICTIONARY METHOD
stock_list.pop('cake')
print(stock_list)
print()
#Dict comprehension

numbers = dict(first = 1, second = 2, third = 3)

sq_numbers = {key: val**2  for key,val in numbers.items()}
print (sq_numbers)

calling = dict(first='hi', second='there', third='you', fourth='loser')

yelling = {num: word.upper()  for num, word in calling.items()}

sentence = ' '.join(yelling.values())
print(sentence)

sentence2 = f"{yelling['first']} {yelling['second']}, {yelling['third']} {yelling['fourth']}!"
print(sentence2)

num_list = [1,2,3,4]

nume_o = {i: 'even' if i%2 == 0 else 'odd'  for i in num_list}
print(nume_o)
numek = {i: 'even'  for i in num_list if i %2==0 }
print(numek)

l = ["CA", "NJ", "RI"]
l2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {l[i]: l2[i]  for i in range(0, len(l))}
print(answer)

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {k: v  for k,v in person}
print(answer)

# make sure your solution is assigned to the answer variable so the tests can work!
answer = dict.fromkeys('aeiou', 0)
print(answer)

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {i: chr(i)  for i in range(65, 91)}
print(answer)
