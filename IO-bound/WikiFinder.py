import urllib.request
import concurrent.futures
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from tqdm import tqdm


def save_links_to_file():
    url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'
    res = open('res.txt', 'w', encoding='utf8')
    for i in tqdm(range(100)):
        html = urlopen(url).read().decode('utf8')
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a')

        for link in links:
            href = link.get('href')
            if href and href.startswith('http') and 'wiki' not in href:
                print(href, file=res)


def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


def parse_links():
    links = open('res.txt', encoding='utf8').read().split('\n')

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(load_url, url, 60): url for url in links}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('%r page is %d bytes' % (url, len(data)))


def main():
    # save_links_to_file()
    parse_links()


if __name__ == '__main__':
    main()
