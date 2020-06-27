import aiohttp
import asyncio
from bs4 import BeautifulSoup
from decorators import logtime

urls = [
    'https://readmha.com/chapter/boku-no-hero-academia-chapter-277',
    'https://readsololeveling.org/chapter/solo-leveling-chapter-112/',
    'https://readkaguyasama.com/chapter/kaguya-sama-love-is-war-chapter-194/',
    'https://readchainsawman.com/chapter/chainsaw-man-chapter-76/'
]


async def fetch(session, url):
    async with session.get(url) as response:
        if response.status == 404:
            print('404')
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
    if soup.findAll('img', src='https://i.imgur.com/MXUX5T4.jpg'):
        print('nie ma')
    else:
        print('jest')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([main(url) for url in urls]))
