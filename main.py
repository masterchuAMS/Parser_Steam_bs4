import requests
from bs4 import BeautifulSoup
import sqlite3

def main():
    connection = sqlite3.connect('games.db')
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT,
            game TEXT
        )
    """)
    connection.close()

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
'''
response_json = requests.get(url).json()

soup = BeautifulSoup(response_json['results_html'], 'lxml')

game_titles = soup.find_all('span', attrs={'class':'title'})


print(
    tuple(
        map (
            lambda game_title:game_title.text,
            game_titles,
        )
    )
)
'''
main()