import asyncio

import aiohttp
from bs4 import BeautifulSoup

from scripts.urls import urls


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main(url):
    async with aiohttp.ClientSession() as session:
        await extract_text(await fetch(session, url))


async def soup_maker(html, display_result=False):
    soup = BeautifulSoup(html, 'html.parser')
    if display_result:
        print(soup.prettify())
    return soup


async def extract_text(html):
    soup = await soup_maker(html)
    print(soup.find('h1', class_='text-white mb-3 uppercase sm:text-lg md:text-3xl').text)
    if soup.findAll('img', src='https://i.imgur.com/MXUX5T4.jpg'):
        print('nie ma')
    else:
        print('jest')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([main(url) for url in urls]))
