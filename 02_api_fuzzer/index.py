import requests
import sys

LINK = "http://localhost:5000/"

sys.setrecursionlimit(100000)

words = []

with open("raft-small-words.txt", "r") as file:
    for line in file:
        words.append(line.strip())

def loop():

    for i, word in enumerate(words):
        url = (f"{LINK}{word}")
        res = requests.get(url)

        if i % 250 == 0:
            print(i) 

        if res.status_code != 404:
            print(f"id: {i} | {word} | {res.status_code} \n")
        elif res.status_code == 404:
            continue

loop()










