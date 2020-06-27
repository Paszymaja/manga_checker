import aiohttp
import asyncio

urls = [
    'https://readmha.com/chapter/boku-no-hero-academia-chapter-277',
    'https://readsololeveling.org/chapter/solo-leveling-chapter-112/',
    'https://readkaguyasama.com/chapter/kaguya-sama-love-is-war-chapter-194/',
    'https://readchainsawman.com/chapter/chainsaw-man-chapter-76/'
]


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        print(html)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([main(url) for url in urls]))
