import csv
import requests

def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    status_code = response.status_code
    print(f'Status code: {status_code}')
    if status_code == 200:
        json_data = response.json()
        for post in json_data:
            print("Post title:", post['title'])


def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    status_code = response.status_code
    posts = response.json()
    if status_code == 200:
        dic = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
             for post in posts
        ]
        with open('posts.csv', 'w', newline="", encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(dic)
