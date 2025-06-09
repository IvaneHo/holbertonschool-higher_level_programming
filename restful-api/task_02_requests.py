#!/usr/bin/python3
"""Fetch and process API data from JSONPlaceholder"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetches posts from the JSONPlaceholder API and prints the titles.
    Also prints the response status code.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        try:
            posts = response.json()
            for post in posts:
                print(post.get('title', ''))
        except ValueError:
            print("Failed to decode JSON response.")


def fetch_and_save_posts():
    """
    Fetches posts and writes selected data (id, title, body) into posts.csv
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            posts = response.json()
            data = [
                {
                    'id': post.get('id'),
                    'title': post.get('title'),
                    'body': post.get('body')
                } for post in posts
            ]

            with open("posts.csv", mode="w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
                writer.writeheader()
                writer.writerows(data)

        except (ValueError, KeyError):
            pass  # silently ignore bad JSON or malformed entries
