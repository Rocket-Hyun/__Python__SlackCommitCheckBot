# parser.py
import requests
from bs4 import BeautifulSoup

def commit_checker(repository_url):
    # HTTP GET Request
    req = requests.get(repository_url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    blocks = soup.find('rect',{"data-date":"2017-11-11"})
    if(blocks.get("fill") == "#7bc96f"):
        return True
    else:
        return False