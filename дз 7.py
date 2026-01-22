import requests
base_url = "https://www.coindesk.com/"
reponse = requests.get(f"{base_url}/posts")

if reponse.status_code == 200:
    posts = reponse.json()[:5]
    for post in posts:
        print(f"Заголовок: {post['title']}")
        print(f"Тело: {post['body']}\n")
else:
    print(f"Ошибка:{reponse.status_code}")