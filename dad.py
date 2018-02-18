import requests
from random import randint

url1 = "https://icanhazdadjoke.com/"
url2 = "https://icanhazdadjoke.com/search"

user_term = input("Let me tell you a joke!  Give me a topic: ")

res2 = requests.get(
    url2, 
    headers={"Accept": "application/json"},
    params={"term": user_term}
).json()

len_res2 = res2['total_jokes']

if not len_res2:
    print(f"Sorry, I ain't got no jokes about {user_term}!  Try again.")
elif len_res2 == 1:
    print(f"I got one joke about {user_term}. Here it is:\n {res2['results'][0]['joke']}")
else:
    joke_index = randint(0, (len_res2 - 1))
    print(f"I got {len_res2} jokes about {user_term}. Here's one:\n {res2['results'][joke_index]['joke']}")
