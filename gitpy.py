import requests


base = 'https://api.github.com/'

def get_events(username):

    url = f"{base}/users/{username}/events"

    response = requests.get(url)
    print(response)

username = input(str("enter username: "))
get_events(username)
    

