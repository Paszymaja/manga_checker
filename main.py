import aiohttp
import asyncio
import async_timeout
from bs4 import BeautifulSoup


async def fetch(session, url):
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()


async def soup_d(html, display_result=False):
    soup = BeautifulSoup(html, 'lxml')
    if display_result:
        print(soup.prettify())
    return soup


async def manga_checker(html):
    soup = await soup_d(html)
    spoiler_image = soup.find('img')
