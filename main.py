import asyncio

import aiohttp
import requests
from bs4 import BeautifulSoup

from scripts.urls import urls as urls_list


class AsynchronousStrategy:
    def __init__(self, url):
        self.url = url

    @staticmethod
    async def fetch(session, url):
        async with session.get(url) as response:
            return await response.text()

    @staticmethod
    async def soup_maker(html, display_result=False):
        soup = BeautifulSoup(html, 'html.parser')
        if display_result:
            print(soup.prettify())
        return soup

    async def extract_text(self, html):
        soup = await self.soup_maker(html)
        print(soup.find('h1', class_='text-white mb-3 uppercase sm:text-lg md:text-3xl').text)
        if soup.findAll('img', src='https://i.imgur.com/MXUX5T4.jpg'):
            print('nie ma')
        else:
            print('jest')

    async def manga_checker(self):
        async with aiohttp.ClientSession() as session:
            await self.extract_text(await self.fetch(session, self.url))


class SynchronousStrategy:
    def __init__(self, urls):
        self.urls = urls

    def manga_checker(self):
        for url in self.urls:
            r = requests.get(url)
            print(f'''{url.split('/')[2]} ''')
            soup = BeautifulSoup(r.content, 'html.parser')
            if r.status_code == 404:
                print('404 nie ma')
                yield '404 nie ma'
            elif soup.findAll('img', src='https://i.imgur.com/MXUX5T4.jpg'):
                yield 'nie ma'
            else:
                yield 'jest'


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([AsynchronousStrategy(url).manga_checker() for url in urls_list]))
