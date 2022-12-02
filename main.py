import requests
from bs4 import BeautifulSoup

url = (
    'https://store.steampowered.com/search/results/?'
    'query&'
    'start=50&'
    'count=50&'
    'dynamic_data=&'
    'sort_by=_ASC&'
    'term=strategy&'
    'snr=1_7_7_151_7&'
    'supportedlang=russian&'
    'infinite=1'
)
def main(url):
    response = requests.get(url).json()
    soup = BeautifulSoup(response['results_html'], 'lxml')
    game_titles = soup.find_all('span', attrs={'class': 'title'})

    print(
        tuple(
            map(
                lambda game_title: game_title.text,
                game_titles,
            )
        )
    )

if __name__=='__main__':
    main(url)