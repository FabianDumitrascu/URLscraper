import requests 
from bs4 import BeautifulSoup

url = 'https://nos.nl/artikel/2530107-veldbestormers-ontruiming-en-afgekeurde-goal-na-2-uur-marokko-wint-absurd-duel-op-spelen'


def get_text_from_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    main_content = soup.body.find('main')
    target_divs = []

    for div in main_content.find_all('div', recursive=False):
        if len(div.find_all('p')) == 1:
            target_divs.append(div)

    result = ''

    for div in target_divs:
        result += div.get_text() + ' '
    return result

def get_title_from_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    title = str(soup.title)
    title = title.replace('<title>', ' ').replace('</title>', '').strip()
    return title

print(get_title_from_url(url), '/n')
print(get_text_from_url(url))






