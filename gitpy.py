import requests
import json
import keyring

base = 'https://api.github.com/'
SERVICE = 'GitCLI'
KEY = 'username'

def login():
    username = keyring.get_password(SERVICE, KEY)

    if username:

        return username

    username = input("Enter username: ").strip()
    keyring.set_password(SERVICE, KEY, username)

    return username




def get_events(username):

    url = f"{base}/users/{username}/events"

    response = requests.get(url)
    events = response.json()
    
    for event in events:
        print(event["type"], "->", event["repo"]["name"], "AT THE TIME: ", event["created_at"])



def main():
    username = login()
    get_events(username)



if __name__ == "__main__":
    main()

