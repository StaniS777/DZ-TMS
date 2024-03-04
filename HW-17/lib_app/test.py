import requests


res = requests.request(
    "GET",
    "https://google.com",
)

print(res)
