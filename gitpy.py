import requests
import json
import argparse

base = 'https://api.github.com/'

def get_events(username):
    url = f"{base}/users/{username}/events"

    response = requests.get(url)
    events = response.json()
    
    for event in events:
        print(event["type"], "->", event["repo"]["name"], "AT THE TIME: ", event["created_at"])


def get_repos(username):
    url = f"{base}/users/{username}/repos"
    
    response = requests.get(url)
    events = response.json()

    for event in events:
        print(event["name"], "\n\nDESCRIPTION\n", event["description"])


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--activity", action="store_true")
    parser.add_argument("--username")
    parser.add_argument("--repos", action="store_true")
    args = parser.parse_args()

    if args.activity and not args.username:
        parser.error("--username is required when using --activity")

    return args



def main():
    args = parse_args()
    username = args.username
    if args.activity:
        get_events(username)
    if args.repos:
        get_repos(args.username)

if __name__ == "__main__":
    main()

