import requests
 
url1 = "http://www.google.com"
url2 = "https://icanhazdadjoke.com/"

#url1
response = requests.get(url1)
print(f'Your request to {url1} came back w/ status code {response.status_code}')



