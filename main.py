import requests


def main():
    url_template = 'https://wttr.in/{}?nMTqu&lang=ru'
    article_id = ["london","svo","Череповец"]
    
    for i in article_id:
        url = url_template.format(i)
        payload = {"text": "python"}
        response = requests.get(url, params=payload)
        print(response.text)
        response.raise_for_status()


if __name__ == "__main__":
    main()
