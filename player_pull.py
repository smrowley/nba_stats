from bs4 import BeautifulSoup
import requests

players_page_url = "https://www.basketball-reference.com/players/"

for letter in "abcdefghijklmnopqrstuvwxyz":
    page = requests.get(players_page_url + letter)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    for table_row in soup.find(id = "players").tbody.find_all('tr'):
        #for column in table_row.children:
        #    print(column.string)
        print(list(table_row.children)[0].string)