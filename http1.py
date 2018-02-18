import requests
 
url1 = "http://www.google.com"
url2 = "https://icanhazdadjoke.com/"
url3 = "https://icanhazdadjoke.com/search"


#url1
response = requests.get(url1)
print(f'Your request to {url1} came back w/ status code {response.status_code}\n\n')

#url2
res2 = requests.get(url2, headers={"Accept": "application/json"})
data = res2.json()
#print(data)
print(data['joke'])
print(f'\n\n')


#url3
res3 = requests.get(
    url3, 
    headers={"Accept": "application/json"},
    params={"term": "cat", "limit": 1}
)

data3 = res3.json()
print(data3)

