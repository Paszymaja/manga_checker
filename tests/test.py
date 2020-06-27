import requests
from bs4 import BeautifulSoup

urls = [
    'https://readmha.com/chapter/boku-no-hero-academia-chapter-277',
    'https://readsololeveling.org/chapter/solo-leveling-chapter-112/',
    'https://readkaguyasama.com/chapter/kaguya-sama-love-is-war-chapter-194/',
    'https://readchainsawman.com/chapter/chainsaw-man-chapter-76/'
]


for url in urls:
    r = requests.get(url)
    print(f'''{url.split('/')[2]}: ''')
    if r.status_code == 404:
        print('404 ni ma')
    soup = BeautifulSoup(r.content, 'html.parser')
    if soup.findAll('img', src='https://i.imgur.com/MXUX5T4.jpg'):
        print('nie ma')
    else:
        print('jest')
