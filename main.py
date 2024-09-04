import requests
import urllib.parse

def main():
    url_template = 'https://wttr.in/{}'
    cities = ["london","svo","Череповец"]
    
    query_params = {'nMTqu': '', 'lang': 'ru'}
    encoded_params = urllib.parse.urlencode(query_params)
    
    for city in cities:
        encoded_city = urllib.parse.quote(city)
        url = f"{url_template.format(encoded_city)}?{encoded_params}"
        response = requests.get(url)
        print(response.text)


if __name__ == "__main__":
    main()
