import requests
import urllib.parse

def main():
    url_template = 'https://wttr.in/{}'
    cities = ["london","svo","Череповец"]
    
    query_params = {'nMTqu': '', 'lang': 'ru'}
    
    for city in cities:
        encoded_city = urllib.parse.quote(city)
        url = url_template.format(encoded_city)
        response = requests.get(url, params=query_params)
        status_code = response.status_code
        if status_code == 200:
            print(response.text)
        else:
            print(response.raise_for_status)


if __name__ == "__main__":
    main()
