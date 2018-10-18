from bs4 import BeautifulSoup
import requests
import requests_cache
import re

requests_cache.install_cache('demo_cache')

# 1 questao
def get_page():
    page_req = requests.get("http://www.tce.pi.gov.br").text
    page = BeautifulSoup(page_req, 'html.parser')
    titles =  page.find_all('a', attrs={'class': 'latestnews'})

    return titles

# 2 questao
def main():
    titles = get_page()

    while(True):
        for i, el in enumerate(titles):
            print(str(i+1) + "->" + el.string)
        print("6 -> Sair")

        choose = input()
        if int(choose)==6:
            break

        text = requests.get(titles[int(choose)-1]['href']).text

        page = BeautifulSoup(text, 'html.parser')

        text_w = page.find_all('div', attrs={'class': 'the_post post_content'})[0].text
        print(text_w)

main()
