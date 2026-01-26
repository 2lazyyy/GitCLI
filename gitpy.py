import requests
import json

base = 'https://api.github.com/'
username = input(str("insert username: "))

def get_events(username):

    url = f"{base}/users/{username}/events"

    response = requests.get(url)
    events = response.json()
    
    for event in events:
        print(event["type"], "->", event["repo"]["name"], "AT THE TIME: ", event["created_at"])

get_events(username)
    

