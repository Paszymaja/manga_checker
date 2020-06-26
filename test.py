import requests
from bs4 import BeautifulSoup

urls = [
    'https://ww5.readmha.com/chapter/boku-no-hero-academia-chapter-276/',
    'https://readsololeveling.org/chapter/solo-leveling-chapter-111/',
    'https://readkaguyasama.com/chapter/kaguya-sama-love-is-war-chapter-193/',
    'https://readchainsawman.com/chapter/chainsaw-man-chapter-75/'
]

for url in urls:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    if r := soup.findAll('img', src='https://i.imgur.com/MXUX5T4.jpg'):
        print(r)
        print('nie ma')
    else:
        print('jest')