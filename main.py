import requests


def main():
    url_template = 'https://wttr.in/{}'
    article_id = ["london","svo","Череповец"]
    
    for i in article_id:
        url = f"{url_template.format(i)}?nMTqu&lang=ru"
        response = requests.get(url)
        print(response.text)
        response.raise_for_status()


if __name__ == "__main__":
    main()
