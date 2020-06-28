import requests
from bs4 import BeautifulSoup

from scripts.decorators import logtime
from scripts.urls import urls


@logtime
def main():
    for url in urls:
        r = requests.get(url)
        print(f'''{url.split('/')[2]} ''')
        soup = BeautifulSoup(r.content, 'html.parser')
        if r.status_code == 404:
            print('404 nie ma')
        elif soup.findAll('img', src='https://i.imgur.com/MXUX5T4.jpg'):
            print('nie ma')
        else:
            print('jest')


if __name__ == '__main__':
    main()
