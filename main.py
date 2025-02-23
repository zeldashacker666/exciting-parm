# main.py
import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')
data = response.json()

print("Data fetched from the API:")
print(data[:3])  # Print the first 3 posts
