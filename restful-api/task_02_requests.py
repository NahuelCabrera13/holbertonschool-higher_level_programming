#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {r.status_code}")
    if r.status_code == 200:
        pepe = r.json()

        for pepes in pepe:
            print(pepes['title'])

def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    r.status_code

    data = r.json()
    
    if r.status_code == 200:
        for post in data:
            del post["userId"]

    with open("posts.csv", "w", newline="", encoding="utf-8") as pepito:
         fieldames = ["id", "title", "body"]
         write = csv.DictWriter(pepito, fieldnames=fieldames)
         write.writeheader()
         for post in data:
            write.writerow(post)
            print(post)
