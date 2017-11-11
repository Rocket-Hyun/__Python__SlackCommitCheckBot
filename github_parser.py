# parser.py
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

korean_time = datetime.now() + timedelta(hours=9)
korean_date = korean_time.strftime("%Y-%m-%d")

def commit_checker(repository_url):
    # HTTP GET Request
    req = requests.get(repository_url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    blocks = soup.find('rect',{"data-date":korean_date})
    if(blocks.get("fill") == "#7bc96f"):
        return True
    else:
        return False