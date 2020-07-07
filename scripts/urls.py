import datetime

start_week_urls = [
    ['https://readmha.com/chapter/boku-no-hero-academia-chapter-', 277],
    ['https://readsololeveling.org/chapter/solo-leveling-chapter-', 111],
    ['https://readkaguyasama.com/chapter/kaguya-sama-love-is-war-chapter-', 194],
    ['https://readchainsawman.com/chapter/chainsaw-man-chapter-', 76]
]

start_week = datetime.date(2020, 7, 7).isocalendar()[1]  # 28 week

for url in start_week_urls:
    url[1] -= datetime.datetime.now().isocalendar()[1] - start_week

urls = [url[0] + str(url[1]) for url in start_week_urls]
