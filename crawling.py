import requests
result = requests.get('https://ja.wikipedia.org/wiki/Python')
print(result.text)