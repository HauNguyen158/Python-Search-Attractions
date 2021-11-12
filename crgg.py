import os
import json
import requests
from bs4 import BeautifulSoup

headers_Get = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }

def main():
    url = "https://www.google.com.vn/search?tbm=isch&q=%C4%91%E1%BA%A1i%20n%E1%BB%99i"

    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    results = soup.findAll('div', {'class': 'rg_i'})

    imagelinks = []
    for result in results:
        text = result.text
        print(text)    

main()