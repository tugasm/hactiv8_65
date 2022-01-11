import requests
#method -> post, get, put, delete
url = 'http://google.com'
response = requests.get(url)
print(f'Response returned: {response.status_code}, {response.reason}')
print(response.text)